from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Competition, Training, Competitor, Trainingpresence, Driver, Event, Result, Location
from .forms import CompetitionForm, TrainingForm, CompetitorForm, TrainingpresenceForm, DriverForm, EventForm, ResultForm, LocationForm
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
User = get_user_model()
import datetime
from django.utils import timezone
from django.contrib import messages

class CompetitionListView(ListView):
    model = Competition

    def post(self, request, *args, **kwargs):
        if 'abmelden' in request.POST:
            competition = Competition.objects.get(id=int(request.POST['abmelden']))
            if timezone.now() > competition.sign_in_date:
                message = "Bitte melde Dich bei Deinem Trainer für den Wettkampf '" + competition.name + "' die Anmeldefrist ist abgelaufen."
                messages.error(request, message)
            else:
                message = "Du bist erfolgreich für den Wettkampf '" + competition.name + "' abgemeldet. Bitte beachte die Details unter 'Wie melde ich mich an?'."
                messages.success(request, message)
                competitor = Competitor.objects.filter(competition=int(request.POST['abmelden']), user=request.user)[0]
                competitor.yesorno = False
                competitor.save()
        if 'anmelden' in request.POST:
            competition = Competition.objects.get(id=int(request.POST['anmelden']))
            if timezone.now() > competition.sign_in_date:
                message = "Bitte melde Dich bei Deinem Trainer für den Wettkampf '" + competition.name + "' die Anmeldefrist ist abgelaufen."
                messages.error(request, message)
            else:
                message = "Du bist erfolgreich für den Wettkampf '" + competition.name + "' angemeldet. Bitte beachte die Details unter 'Wie melde ich mich an?'."
                messages.success(request, message)
                competitor = Competitor.objects.filter(competition=int(request.POST['anmelden']), user=request.user)[0]
                competitor.yesorno = True
                competitor.save()
        return redirect('focus:focus_competition_list')

    def get_queryset(self):
        today = datetime.datetime.today()
        return Competition.objects.filter(endtime__gte=today).order_by('starttime')


class CompetitionCreateView(CreateView):
    model = Competition
    form_class = CompetitionForm


class CompetitionDetailView(DetailView):
    model = Competition

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CompetitionDetailView, self).get_context_data(**kwargs)
        context['competitors'] = Competitor.objects.filter(competition=kwargs['object'].pk)
        return context


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
        today = datetime.datetime.today()
        return Training.objects.filter(endtime__gte=today).order_by('starttime')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TrainingListView, self).get_context_data(**kwargs)
        return context


class TrainingCreateView(CreateView):
    model = Training
    form_class = TrainingForm


class TrainingDetailView(DetailView):
    model = Training


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TrainingDetailView, self).get_context_data(**kwargs)
        context['athletes'] = Trainingpresence.objects.filter(training=kwargs['object'].pk)
        return context


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

