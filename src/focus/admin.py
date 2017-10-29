from django.contrib import admin
from django import forms
from .models import Competition, Training, Competitor, Trainingpresence, Driver, Event, Result, Location

class CompetitionAdminForm(forms.ModelForm):

    class Meta:
        model = Competition
        fields = '__all__'


class CompetitionAdmin(admin.ModelAdmin):
    form = CompetitionAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'startime', 'endtime', 'description', 'link', 'sign_in_date', 'meeting_time', 'file', 'car_seats_required', 'car_seats_available']
    #readonly_fields = ['name', 'slug', 'created', 'last_updated', 'startime', 'endtime', 'description', 'link', 'sign_in_date', 'meeting_time', 'file', 'car_seats_required', 'car_seats_available']

admin.site.register(Competition, CompetitionAdmin)


class TrainingAdminForm(forms.ModelForm):

    class Meta:
        model = Training
        fields = '__all__'


class TrainingAdmin(admin.ModelAdmin):
    form = TrainingAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'starttime', 'endtime', 'intensity', 'short_description', 'detailed_description', 'file']
    #readonly_fields = ['name', 'slug', 'created', 'last_updated', 'starttime', 'endtime', 'intensity', 'short_description', 'detailed_description', 'file']

admin.site.register(Training, TrainingAdmin)


class CompetitorAdminForm(forms.ModelForm):

    class Meta:
        model = Competitor
        fields = '__all__'


class CompetitorAdmin(admin.ModelAdmin):
    form = CompetitorAdminForm
    list_display = ['slug', 'created', 'last_updated', 'yesorno', 'note']
    #readonly_fields = ['slug', 'created', 'last_updated', 'yesorno', 'note']

admin.site.register(Competitor, CompetitorAdmin)


class TrainingpresenceAdminForm(forms.ModelForm):

    class Meta:
        model = Trainingpresence
        fields = '__all__'


class TrainingpresenceAdmin(admin.ModelAdmin):
    form = TrainingpresenceAdminForm
    list_display = ['slug', 'created', 'last_updated', 'yesorno', 'excused', 'feedback_to_coach', 'feedback_to_athlete']
    #readonly_fields = ['slug', 'created', 'last_updated', 'yesorno', 'excused', 'feedback_to_coach', 'feedback_to_athlete']

admin.site.register(Trainingpresence, TrainingpresenceAdmin)


class DriverAdminForm(forms.ModelForm):

    class Meta:
        model = Driver
        fields = '__all__'


class DriverAdmin(admin.ModelAdmin):
    form = DriverAdminForm
    list_display = ['slug', 'created', 'last_updated', 'number_seats', 'note']
    #readonly_fields = ['slug', 'created', 'last_updated', 'number_seats', 'note']

admin.site.register(Driver, DriverAdmin)


class EventAdminForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'


class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'short_description', 'file', 'is_duration', 'is_distance', 'is_repetitions', 'detailed_description']
    #readonly_fields = ['name', 'slug', 'created', 'last_updated', 'short_description', 'file', 'is_duration', 'is_distance', 'is_repetitions', 'detailed_description']

admin.site.register(Event, EventAdmin)


class ResultAdminForm(forms.ModelForm):

    class Meta:
        model = Result
        fields = '__all__'


class ResultAdmin(admin.ModelAdmin):
    form = ResultAdminForm
    list_display = ['slug', 'created', 'last_updated', 'duration', 'distance', 'repetitions', 'note']
    #readonly_fields = ['slug', 'created', 'last_updated', 'duration', 'distance', 'repetitions', 'note']

admin.site.register(Result, ResultAdmin)


class LocationAdminForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = '__all__'


class LocationAdmin(admin.ModelAdmin):
    form = LocationAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'address', 'googlemapurl', 'description']
    #readonly_fields = ['name', 'slug', 'created', 'last_updated', 'address', 'googlemapurl', 'description']

admin.site.register(Location, LocationAdmin)


