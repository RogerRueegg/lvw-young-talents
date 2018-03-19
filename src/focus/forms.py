from django import forms
from .models import Competition, Training, Competitor, Trainingpresence, Driver, Event, Result, Location
from datetimewidget.widgets import DateTimeWidget

class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ['name', 'starttime', 'endtime', 'description', 'link', 'sign_in_date', 'subscription', 'selfsubscription', 'meeting_time', 'file', 'car_seats_required', 'car_seats_available', 'location', 'meetingpoint']
        widgets = {
            # Use localization and bootstrap 3
            'starttime': DateTimeWidget(attrs={'id': "starttime"}, options={'format':'yyyy-mm-dd hh:ii'}),
            'endtime': DateTimeWidget(attrs={'id': "endtime"}, options={'format':'yyyy-mm-dd hh:ii'}),
            'sign_in_date': DateTimeWidget(attrs={'id': "starttime"}, options={'format': 'yyyy-mm-dd hh:ii'}),
            'meeting_time': DateTimeWidget(attrs={'id': "endtime"}, options={'format': 'yyyy-mm-dd hh:ii'}),
        }

class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ['name', 'starttime', 'endtime', 'intensity', 'short_description', 'detailed_description', 'file', 'location']
        widgets = {
            # Use localization and bootstrap 3
            'starttime': DateTimeWidget(attrs={'id': "starttime"}, options={'format':'yyyy-mm-dd hh:ii'}),
            'endtime': DateTimeWidget(attrs={'id': "endtime"}, options={'format':'yyyy-mm-dd hh:ii'}),
        }


class CompetitorForm(forms.ModelForm):
    class Meta:
        model = Competitor
        fields = ['yesorno', 'note', 'user', 'competition']


class TrainingpresenceForm(forms.ModelForm):
    class Meta:
        model = Trainingpresence
        fields = ['yesorno', 'excused', 'feedback_to_coach', 'feedback_to_athlete', 'user', 'training']


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['number_seats', 'note', 'user', 'competition']


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'short_description', 'file', 'is_duration', 'is_distance', 'is_repetitions', 'detailed_description']


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['duration', 'distance', 'repetitions', 'note', 'user', 'event', 'location']


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'address', 'googlemapurl', 'description']


