from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField

USER_TYPES = (
    ('Neu','Neu'),
    ('Athlet','Athlet'),
    ('Eltern','Eltern'),
    ('Coach', 'Coach'),
)


class BaseProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                primary_key=True)
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    # Add more user profile fields here. Make sure they are nullable
    # or with default values
    picture = models.ImageField('Profilbild',
                                upload_to='profile_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    bio = models.CharField("Über mich", max_length=200, blank=True, null=True)
    email_verified = models.BooleanField("Email verified", default=False)
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='Neu')
    active = models.BooleanField(default=True)
    bdate = models.DateField("Geburtsdatum",auto_now=False, auto_now_add=False, blank=True, null=True, default='2099-01-20')
    phone_number = PhoneNumberField("Natelnummer",blank=True, null=True, default='+41791234678')
    street = models.CharField(max_length=255, blank=True, null=True, default='Marktgasse 1')
    city = models.CharField(max_length=255, blank=True, null=True, default='8400 Winterthur')

    class Meta:
        abstract = True

    @property
    def is_coach(self):
        if self.user_type == 'Coach':
            return True
        else:
            return False


@python_2_unicode_compatible
class Profile(BaseProfile):
    def __str__(self):
        return "{}'s profile". format(self.user)
