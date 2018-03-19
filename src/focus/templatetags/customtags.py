from django import template
from focus.models import Trainingpresence, Competitor

register = template.Library()

def trainingpresence(training, user):
    presence, created = Trainingpresence.objects.get_or_create(user=user, training=training)
    return presence.excused

register.filter('trainingpresence', trainingpresence)

def competitor(competition, user):
    competitor, created = Competitor.objects.get_or_create(user=user, competition=competition)
    return competitor.yesorno

register.filter('competitor', competitor)

def strday(dayofweek):
    days = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
    return days[dayofweek]

register.filter('strday', strday)