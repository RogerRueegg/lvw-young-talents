from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Competition, Training, Competitor, Trainingpresence, Driver, Event, Result, Location
from .forms import CompetitionForm, TrainingForm, CompetitorForm, TrainingpresenceForm, DriverForm, EventForm, ResultForm, LocationForm
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
User = get_user_model()
import datetime

class CompetitionListView(ListView):
    model = Competition

    def post(self, request, *args, **kwargs):
        if 'abmelden' in request.POST:
            competitor = Competitor.objects.filter(competition=int(request.POST['abmelden']), user=request.user)[0]
            competitor.yesorno = False
            competitor.save()
        if 'anmelden' in request.POST:
            competitor = Competitor.objects.filter(competition=int(request.POST['anmelden']), user=request.user)[0]
            competitor.yesorno = True
            competitor.save()
        return redirect('focus:focus_competition_list')

    def get_queryset(self):
        today = datetime.datetime.today()
        return Competition.objects.filter(endtime__gte=today)


class CompetitionCreateView(CreateView):
    model = Competition
    form_class = CompetitionForm


class CompetitionDetailView(DetailView):
    model = Competition


class CompetitionUpdateView(UpdateView):
    model = Competition
    form_class = CompetitionForm


class TrainingListView(ListView):
    model = Training

    def post(self, request, *args, **kwargs):
        if 'abmelden' in request.POST:
            presence = Trainingpresence.objects.filter(training=int(request.POST['abmelden']), user=request.user)[0]
            presence.excused = True
            presence.yesorno = False
            presence.save()
        if 'anmelden' in request.POST:
            presence = Trainingpresence.objects.filter(training=int(request.POST['anmelden']), user=request.user)[0]
            presence.excused = False
            presence.yesorno = True
            presence.save()
        return redirect('focus:focus_training_list')


    def get_queryset(self):
        a = 1
        today = datetime.datetime.today()
        return Training.objects.filter(endtime__gte=today)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TrainingListView, self).get_context_data(**kwargs)
        return context


class TrainingCreateView(CreateView):
    model = Training
    form_class = TrainingForm


class TrainingDetailView(DetailView):
    model = Training


class TrainingUpdateView(UpdateView):
    model = Training
    form_class = TrainingForm


class CompetitorListView(ListView):
    model = Competitor


class CompetitorCreateView(CreateView):
    model = Competitor
    form_class = CompetitorForm


class CompetitorDetailView(DetailView):
    model = Competitor


class CompetitorUpdateView(UpdateView):
    model = Competitor
    form_class = CompetitorForm


class TrainingpresenceListView(ListView):
    model = Trainingpresence


class TrainingpresenceCreateView(CreateView):
    model = Trainingpresence
    form_class = TrainingpresenceForm


class TrainingpresenceDetailView(DetailView):
    model = Trainingpresence


class TrainingpresenceUpdateView(UpdateView):
    model = Trainingpresence
    form_class = TrainingpresenceForm


class DriverListView(ListView):
    model = Driver


class DriverCreateView(CreateView):
    model = Driver
    form_class = DriverForm


class DriverDetailView(DetailView):
    model = Driver


class DriverUpdateView(UpdateView):
    model = Driver
    form_class = DriverForm


class EventListView(ListView):
    model = Event


class EventCreateView(CreateView):
    model = Event
    form_class = EventForm


class EventDetailView(DetailView):
    model = Event


class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm


class ResultListView(ListView):
    model = Result


class ResultCreateView(CreateView):
    model = Result
    form_class = ResultForm


class ResultDetailView(DetailView):
    model = Result


class ResultUpdateView(UpdateView):
    model = Result
    form_class = ResultForm


class LocationListView(ListView):
    model = Location


class LocationCreateView(CreateView):
    model = Location
    form_class = LocationForm


class LocationDetailView(DetailView):
    model = Location


class LocationUpdateView(UpdateView):
    model = Location
    form_class = LocationForm

