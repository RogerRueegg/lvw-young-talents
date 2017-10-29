from . import models

from rest_framework import serializers


class CompetitionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Competition
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'startime', 
            'endtime', 
            'description', 
            'link', 
            'sign_in_date', 
            'meeting_time', 
            'file', 
            'car_seats_required', 
            'car_seats_available', 
        )


class TrainingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Training
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'starttime', 
            'endtime', 
            'intensity', 
            'short_description', 
            'detailed_description', 
            'file', 
        )


class CompetitorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Competitor
        fields = (
            'slug', 
            'created', 
            'last_updated', 
            'yesorno', 
            'note', 
        )


class TrainingpresenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Trainingpresence
        fields = (
            'slug', 
            'created', 
            'last_updated', 
            'yesorno', 
            'excused', 
            'feedback_to_coach', 
            'feedback_to_athlete', 
        )


class DriverSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Driver
        fields = (
            'slug', 
            'created', 
            'last_updated', 
            'number_seats', 
            'note', 
        )


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Event
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'short_description', 
            'file', 
            'is_duration', 
            'is_distance', 
            'is_repetitions', 
            'detailed_description', 
        )


class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Result
        fields = (
            'slug', 
            'created', 
            'last_updated', 
            'duration', 
            'distance', 
            'repetitions', 
            'note', 
        )


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Location
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'address', 
            'googlemapurl', 
            'description', 
        )


