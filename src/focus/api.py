from . import models
from . import serializers
from rest_framework import viewsets, permissions


class CompetitionViewSet(viewsets.ModelViewSet):
    """ViewSet for the Competition class"""

    queryset = models.Competition.objects.all()
    serializer_class = serializers.CompetitionSerializer
    permission_classes = [permissions.IsAuthenticated]


class TrainingViewSet(viewsets.ModelViewSet):
    """ViewSet for the Training class"""

    queryset = models.Training.objects.all()
    serializer_class = serializers.TrainingSerializer
    permission_classes = [permissions.IsAuthenticated]


class CompetitorViewSet(viewsets.ModelViewSet):
    """ViewSet for the Competitor class"""

    queryset = models.Competitor.objects.all()
    serializer_class = serializers.CompetitorSerializer
    permission_classes = [permissions.IsAuthenticated]


class TrainingpresenceViewSet(viewsets.ModelViewSet):
    """ViewSet for the Trainingpresence class"""

    queryset = models.Trainingpresence.objects.all()
    serializer_class = serializers.TrainingpresenceSerializer
    permission_classes = [permissions.IsAuthenticated]


class DriverViewSet(viewsets.ModelViewSet):
    """ViewSet for the Driver class"""

    queryset = models.Driver.objects.all()
    serializer_class = serializers.DriverSerializer
    permission_classes = [permissions.IsAuthenticated]


class EventViewSet(viewsets.ModelViewSet):
    """ViewSet for the Event class"""

    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer
    permission_classes = [permissions.IsAuthenticated]


class ResultViewSet(viewsets.ModelViewSet):
    """ViewSet for the Result class"""

    queryset = models.Result.objects.all()
    serializer_class = serializers.ResultSerializer
    permission_classes = [permissions.IsAuthenticated]


class LocationViewSet(viewsets.ModelViewSet):
    """ViewSet for the Location class"""

    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerializer
    permission_classes = [permissions.IsAuthenticated]


