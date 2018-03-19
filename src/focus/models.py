from django.core.urlresolvers import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class Competition(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    starttime = models.DateTimeField(blank=True, null=True)
    endtime = models.DateTimeField(blank=True, null=True)
    description = models.TextField(max_length=2000)
    subscription = models.TextField(max_length=2000, blank=True, null=True)
    selfsubscription = models.BooleanField(default=False)
    link = models.URLField(blank=True, null=True)
    sign_in_date = models.DateTimeField(null=True, blank=True)
    meeting_time = models.DateTimeField(null=True, blank=True)
    file = models.FileField(upload_to="competitions/", null=True, blank=True)
    car_seats_required = models.IntegerField(blank=True, null=True)
    car_seats_available = models.IntegerField(blank=True, null=True)

    # Relationship Fields
    location = models.ForeignKey('focus.Location', related_name='competition_location')
    meetingpoint = models.ForeignKey('focus.Location', null=True, blank=True, related_name='competition_meetingpoint')

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def __str__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('focus:focus_competition_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('focus:focus_competition_update', args=(self.slug,))

    def file_link(self):
        if self.file:
            return "<a href='%s'>download</a>" % (self.file.url,)
        else:
            return ""

    file_link.allow_tags = True


class Training(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    intensity = models.CharField(max_length=20, choices=(('Low','Low'),('Medium','Medium'),('High','High'),('Regeneration','Regeneration')), default='High')
    short_description = models.CharField(max_length=200)
    detailed_description = models.TextField(max_length=4000)
    file = models.FileField(upload_to="trainings/", blank=True, null=True)

    # Relationship Fields
    location = models.ForeignKey('focus.Location', )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def __str__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('focus:focus_training_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('focus:focus_training_update', args=(self.slug,))

    def change_status(self, user):
        tp = Trainingpresence.objects.filter(id=self.id, user=user)
        if tp:
            if tp.excused:
                tp.excused=False
            else:
                tp.excused=True
            tp.save()

    def file_link(self):
        if self.file:
            return "<a href='%s'>download</a>" % (self.file.url,)
        else:
            return ""

class Competitor(models.Model):

    # Fields
    slug = extension_fields.AutoSlugField(populate_from='competition', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    yesorno = models.BooleanField(default=False)
    note = models.TextField(max_length=300, blank=True, null=True)

    # Relationship Fields
    user = models.ForeignKey(settings.AUTH_USER_MODEL, )
    competition = models.ForeignKey('focus.Competition', )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def __str__(self):
        return u'%s' % self.user.name

    def get_absolute_url(self):
        return reverse('focus_competitor_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('focus_competitor_update', args=(self.slug,))


class Trainingpresence(models.Model):

    # Fields
    slug = extension_fields.AutoSlugField(populate_from='training', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    yesorno = models.BooleanField(default=True)
    excused = models.BooleanField(default=False)
    feedback_to_coach = models.TextField(max_length=2000, blank=True, null=True)
    feedback_to_athlete = models.TextField(max_length=2000, blank=True, null=True)

    # Relationship Fields
    user = models.ForeignKey(settings.AUTH_USER_MODEL, )
    training = models.ForeignKey('focus.Training', )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('focus_trainingpresence_detail', args=(self.slug,))

    def get_prescence(self, user):
        presence, created = Trainingpresence.objects.get_or_create(user=user, training=self)
        return presence

    def get_update_url(self):
        return reverse('focus_trainingpresence_update', args=(self.slug,))


class Driver(models.Model):

    # Fields
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    number_seats = models.IntegerField(default=0)
    note = models.TextField(max_length=200, blank=True, null=True)

    # Relationship Fields
    user = models.ForeignKey(settings.AUTH_USER_MODEL, )
    competition = models.ForeignKey('focus.Competition', )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('focus_driver_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('focus_driver_update', args=(self.slug,))


class Event(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    short_description = models.CharField(max_length=200, null=True, blank=True)
    file = models.FileField(upload_to="events/", blank=True, null=True)
    is_duration = models.BooleanField(default=False)
    is_distance = models.BooleanField(default=False)
    is_repetitions = models.BooleanField(default=False)
    detailed_description = models.TextField(max_length=2000, blank=True, null=True)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def __str__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('focus_event_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('focus_event_update', args=(self.slug,))


class Result(models.Model):

    # Fields
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    duration = models.DurationField(blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)
    repetitions = models.IntegerField(blank=True, null=True)
    note = models.TextField(max_length=300, blank=True, null=True)

    # Relationship Fields
    user = models.ForeignKey(settings.AUTH_USER_MODEL, )
    event = models.ForeignKey('focus.Event', )
    location = models.ForeignKey('focus.Location', blank=True, null=True)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('focus_result_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('focus_result_update', args=(self.slug,))


class Location(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    address = models.TextField(max_length=300)
    googlemapurl = models.URLField(null=True, blank=True)
    description = models.TextField(max_length=300, blank=True, null=True)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def __str__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('focus:focus_location_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('focus:focus_location_update', args=(self.slug,))


