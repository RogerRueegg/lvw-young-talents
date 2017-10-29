import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import Competition, Training, Competitor, Trainingpresence, Driver, Event, Result, Location
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_competition(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["startime"] = "startime"
    defaults["endtime"] = "endtime"
    defaults["description"] = "description"
    defaults["link"] = "link"
    defaults["sign_in_date"] = "sign_in_date"
    defaults["meeting_time"] = "meeting_time"
    defaults["file"] = "file"
    defaults["car_seats_required"] = "car_seats_required"
    defaults["car_seats_available"] = "car_seats_available"
    defaults.update(**kwargs)
    if "location" not in defaults:
        defaults["location"] = create_location()
    if "meetingpoint" not in defaults:
        defaults["meetingpoint"] = create_location()
    return Competition.objects.create(**defaults)


def create_training(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["starttime"] = "starttime"
    defaults["endtime"] = "endtime"
    defaults["intensity"] = "intensity"
    defaults["short_description"] = "short_description"
    defaults["detailed_description"] = "detailed_description"
    defaults["file"] = "file"
    defaults.update(**kwargs)
    if "location" not in defaults:
        defaults["location"] = create_location()
    return Training.objects.create(**defaults)


def create_competitor(**kwargs):
    defaults = {}
    defaults["yesorno"] = "yesorno"
    defaults["note"] = "note"
    defaults.update(**kwargs)
    if "user" not in defaults:
        defaults["user"] = create_django_contrib_auth_models_user()
    if "competition" not in defaults:
        defaults["competition"] = create_competition()
    return Competitor.objects.create(**defaults)


def create_trainingpresence(**kwargs):
    defaults = {}
    defaults["yesorno"] = "yesorno"
    defaults["excused"] = "excused"
    defaults["feedback_to_coach"] = "feedback_to_coach"
    defaults["feedback_to_athlete"] = "feedback_to_athlete"
    defaults.update(**kwargs)
    if "user" not in defaults:
        defaults["user"] = create_django_contrib_auth_models_user()
    if "training" not in defaults:
        defaults["training"] = create_training()
    return Trainingpresence.objects.create(**defaults)


def create_driver(**kwargs):
    defaults = {}
    defaults["number_seats"] = "number_seats"
    defaults["note"] = "note"
    defaults.update(**kwargs)
    if "user" not in defaults:
        defaults["user"] = create_django_contrib_auth_models_user()
    if "competition" not in defaults:
        defaults["competition"] = create_competition()
    return Driver.objects.create(**defaults)


def create_event(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["short_description"] = "short_description"
    defaults["file"] = "file"
    defaults["is_duration"] = "is_duration"
    defaults["is_distance"] = "is_distance"
    defaults["is_repetitions"] = "is_repetitions"
    defaults["detailed_description"] = "detailed_description"
    defaults.update(**kwargs)
    return Event.objects.create(**defaults)


def create_result(**kwargs):
    defaults = {}
    defaults["duration"] = "duration"
    defaults["distance"] = "distance"
    defaults["repetitions"] = "repetitions"
    defaults["note"] = "note"
    defaults.update(**kwargs)
    if "user" not in defaults:
        defaults["user"] = create_django_contrib_auth_models_user()
    if "event" not in defaults:
        defaults["event"] = create_event()
    if "location" not in defaults:
        defaults["location"] = create_location()
    return Result.objects.create(**defaults)


def create_location(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["address"] = "address"
    defaults["googlemapurl"] = "googlemapurl"
    defaults["description"] = "description"
    defaults.update(**kwargs)
    return Location.objects.create(**defaults)


class CompetitionViewTest(unittest.TestCase):
    '''
    Tests for Competition
    '''
    def setUp(self):
        self.client = Client()

    def test_list_competition(self):
        url = reverse('focus_competition_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_competition(self):
        url = reverse('focus_competition_create')
        data = {
            "name": "name",
            "startime": "startime",
            "endtime": "endtime",
            "description": "description",
            "link": "link",
            "sign_in_date": "sign_in_date",
            "meeting_time": "meeting_time",
            "file": "file",
            "car_seats_required": "car_seats_required",
            "car_seats_available": "car_seats_available",
            "location": create_location().pk,
            "meetingpoint": create_location().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_competition(self):
        competition = create_competition()
        url = reverse('focus_competition_detail', args=[competition.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_competition(self):
        competition = create_competition()
        data = {
            "name": "name",
            "startime": "startime",
            "endtime": "endtime",
            "description": "description",
            "link": "link",
            "sign_in_date": "sign_in_date",
            "meeting_time": "meeting_time",
            "file": "file",
            "car_seats_required": "car_seats_required",
            "car_seats_available": "car_seats_available",
            "location": create_location().pk,
            "meetingpoint": create_location().pk,
        }
        url = reverse('focus_competition_update', args=[competition.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class TrainingViewTest(unittest.TestCase):
    '''
    Tests for Training
    '''
    def setUp(self):
        self.client = Client()

    def test_list_training(self):
        url = reverse('focus_training_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_training(self):
        url = reverse('focus_training_create')
        data = {
            "name": "name",
            "starttime": "starttime",
            "endtime": "endtime",
            "intensity": "intensity",
            "short_description": "short_description",
            "detailed_description": "detailed_description",
            "file": "file",
            "location": create_location().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_training(self):
        training = create_training()
        url = reverse('focus_training_detail', args=[training.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_training(self):
        training = create_training()
        data = {
            "name": "name",
            "starttime": "starttime",
            "endtime": "endtime",
            "intensity": "intensity",
            "short_description": "short_description",
            "detailed_description": "detailed_description",
            "file": "file",
            "location": create_location().pk,
        }
        url = reverse('focus_training_update', args=[training.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CompetitorViewTest(unittest.TestCase):
    '''
    Tests for Competitor
    '''
    def setUp(self):
        self.client = Client()

    def test_list_competitor(self):
        url = reverse('focus_competitor_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_competitor(self):
        url = reverse('focus_competitor_create')
        data = {
            "yesorno": "yesorno",
            "note": "note",
            "user": create_django_contrib_auth_models_user().pk,
            "competition": create_competition().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_competitor(self):
        competitor = create_competitor()
        url = reverse('focus_competitor_detail', args=[competitor.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_competitor(self):
        competitor = create_competitor()
        data = {
            "yesorno": "yesorno",
            "note": "note",
            "user": create_django_contrib_auth_models_user().pk,
            "competition": create_competition().pk,
        }
        url = reverse('focus_competitor_update', args=[competitor.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class TrainingpresenceViewTest(unittest.TestCase):
    '''
    Tests for Trainingpresence
    '''
    def setUp(self):
        self.client = Client()

    def test_list_trainingpresence(self):
        url = reverse('focus_trainingpresence_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_trainingpresence(self):
        url = reverse('focus_trainingpresence_create')
        data = {
            "yesorno": "yesorno",
            "excused": "excused",
            "feedback_to_coach": "feedback_to_coach",
            "feedback_to_athlete": "feedback_to_athlete",
            "user": create_django_contrib_auth_models_user().pk,
            "training": create_training().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_trainingpresence(self):
        trainingpresence = create_trainingpresence()
        url = reverse('focus_trainingpresence_detail', args=[trainingpresence.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_trainingpresence(self):
        trainingpresence = create_trainingpresence()
        data = {
            "yesorno": "yesorno",
            "excused": "excused",
            "feedback_to_coach": "feedback_to_coach",
            "feedback_to_athlete": "feedback_to_athlete",
            "user": create_django_contrib_auth_models_user().pk,
            "training": create_training().pk,
        }
        url = reverse('focus_trainingpresence_update', args=[trainingpresence.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class DriverViewTest(unittest.TestCase):
    '''
    Tests for Driver
    '''
    def setUp(self):
        self.client = Client()

    def test_list_driver(self):
        url = reverse('focus_driver_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_driver(self):
        url = reverse('focus_driver_create')
        data = {
            "number_seats": "number_seats",
            "note": "note",
            "user": create_django_contrib_auth_models_user().pk,
            "competition": create_competition().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_driver(self):
        driver = create_driver()
        url = reverse('focus_driver_detail', args=[driver.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_driver(self):
        driver = create_driver()
        data = {
            "number_seats": "number_seats",
            "note": "note",
            "user": create_django_contrib_auth_models_user().pk,
            "competition": create_competition().pk,
        }
        url = reverse('focus_driver_update', args=[driver.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class EventViewTest(unittest.TestCase):
    '''
    Tests for Event
    '''
    def setUp(self):
        self.client = Client()

    def test_list_event(self):
        url = reverse('focus_event_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_event(self):
        url = reverse('focus_event_create')
        data = {
            "name": "name",
            "short_description": "short_description",
            "file": "file",
            "is_duration": "is_duration",
            "is_distance": "is_distance",
            "is_repetitions": "is_repetitions",
            "detailed_description": "detailed_description",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_event(self):
        event = create_event()
        url = reverse('focus_event_detail', args=[event.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_event(self):
        event = create_event()
        data = {
            "name": "name",
            "short_description": "short_description",
            "file": "file",
            "is_duration": "is_duration",
            "is_distance": "is_distance",
            "is_repetitions": "is_repetitions",
            "detailed_description": "detailed_description",
        }
        url = reverse('focus_event_update', args=[event.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ResultViewTest(unittest.TestCase):
    '''
    Tests for Result
    '''
    def setUp(self):
        self.client = Client()

    def test_list_result(self):
        url = reverse('focus_result_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_result(self):
        url = reverse('focus_result_create')
        data = {
            "duration": "duration",
            "distance": "distance",
            "repetitions": "repetitions",
            "note": "note",
            "user": create_django_contrib_auth_models_user().pk,
            "event": create_event().pk,
            "location": create_location().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_result(self):
        result = create_result()
        url = reverse('focus_result_detail', args=[result.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_result(self):
        result = create_result()
        data = {
            "duration": "duration",
            "distance": "distance",
            "repetitions": "repetitions",
            "note": "note",
            "user": create_django_contrib_auth_models_user().pk,
            "event": create_event().pk,
            "location": create_location().pk,
        }
        url = reverse('focus_result_update', args=[result.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class LocationViewTest(unittest.TestCase):
    '''
    Tests for Location
    '''
    def setUp(self):
        self.client = Client()

    def test_list_location(self):
        url = reverse('focus_location_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_location(self):
        url = reverse('focus_location_create')
        data = {
            "name": "name",
            "address": "address",
            "googlemapurl": "googlemapurl",
            "description": "description",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_location(self):
        location = create_location()
        url = reverse('focus_location_detail', args=[location.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_location(self):
        location = create_location()
        data = {
            "name": "name",
            "address": "address",
            "googlemapurl": "googlemapurl",
            "description": "description",
        }
        url = reverse('focus_location_update', args=[location.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


