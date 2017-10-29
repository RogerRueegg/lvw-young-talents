from django.conf.urls import url, include
from rest_framework import routers
from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'competition', api.CompetitionViewSet)
router.register(r'training', api.TrainingViewSet)
router.register(r'competitor', api.CompetitorViewSet)
router.register(r'trainingpresence', api.TrainingpresenceViewSet)
router.register(r'driver', api.DriverViewSet)
router.register(r'event', api.EventViewSet)
router.register(r'result', api.ResultViewSet)
router.register(r'location', api.LocationViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Competition
    url(r'^focus/competition/$', views.CompetitionListView.as_view(), name='focus_competition_list'),
    url(r'^focus/competition/create/$', views.CompetitionCreateView.as_view(), name='focus_competition_create'),
    url(r'^focus/competition/detail/(?P<slug>\S+)/$', views.CompetitionDetailView.as_view(), name='focus_competition_detail'),
    url(r'^focus/competition/update/(?P<slug>\S+)/$', views.CompetitionUpdateView.as_view(), name='focus_competition_update'),
)

urlpatterns += (
    # urls for Training
    url(r'^focus/training/$', views.TrainingListView.as_view(), name='focus_training_list'),
    url(r'^focus/training/create/$', views.TrainingCreateView.as_view(), name='focus_training_create'),
    url(r'^focus/training/detail/(?P<slug>\S+)/$', views.TrainingDetailView.as_view(), name='focus_training_detail'),
    url(r'^focus/training/update/(?P<slug>\S+)/$', views.TrainingUpdateView.as_view(), name='focus_training_update'),
)

urlpatterns += (
    # urls for Competitor
    url(r'^focus/competitor/$', views.CompetitorListView.as_view(), name='focus_competitor_list'),
    url(r'^focus/competitor/create/$', views.CompetitorCreateView.as_view(), name='focus_competitor_create'),
    url(r'^focus/competitor/detail/(?P<slug>\S+)/$', views.CompetitorDetailView.as_view(), name='focus_competitor_detail'),
    url(r'^focus/competitor/update/(?P<slug>\S+)/$', views.CompetitorUpdateView.as_view(), name='focus_competitor_update'),
)

urlpatterns += (
    # urls for Trainingpresence
    url(r'^focus/trainingpresence/$', views.TrainingpresenceListView.as_view(), name='focus_trainingpresence_list'),
    url(r'^focus/trainingpresence/create/$', views.TrainingpresenceCreateView.as_view(), name='focus_trainingpresence_create'),
    url(r'^focus/trainingpresence/detail/(?P<slug>\S+)/$', views.TrainingpresenceDetailView.as_view(), name='focus_trainingpresence_detail'),
    url(r'^focus/trainingpresence/update/(?P<slug>\S+)/$', views.TrainingpresenceUpdateView.as_view(), name='focus_trainingpresence_update'),
)

urlpatterns += (
    # urls for Driver
    url(r'^focus/driver/$', views.DriverListView.as_view(), name='focus_driver_list'),
    url(r'^focus/driver/create/$', views.DriverCreateView.as_view(), name='focus_driver_create'),
    url(r'^focus/driver/detail/(?P<slug>\S+)/$', views.DriverDetailView.as_view(), name='focus_driver_detail'),
    url(r'^focus/driver/update/(?P<slug>\S+)/$', views.DriverUpdateView.as_view(), name='focus_driver_update'),
)

urlpatterns += (
    # urls for Event
    url(r'^focus/event/$', views.EventListView.as_view(), name='focus_event_list'),
    url(r'^focus/event/create/$', views.EventCreateView.as_view(), name='focus_event_create'),
    url(r'^focus/event/detail/(?P<slug>\S+)/$', views.EventDetailView.as_view(), name='focus_event_detail'),
    url(r'^focus/event/update/(?P<slug>\S+)/$', views.EventUpdateView.as_view(), name='focus_event_update'),
)

urlpatterns += (
    # urls for Result
    url(r'^focus/result/$', views.ResultListView.as_view(), name='focus_result_list'),
    url(r'^focus/result/create/$', views.ResultCreateView.as_view(), name='focus_result_create'),
    url(r'^focus/result/detail/(?P<slug>\S+)/$', views.ResultDetailView.as_view(), name='focus_result_detail'),
    url(r'^focus/result/update/(?P<slug>\S+)/$', views.ResultUpdateView.as_view(), name='focus_result_update'),
)

urlpatterns += (
    # urls for Location
    url(r'^focus/location/$', views.LocationListView.as_view(), name='focus_location_list'),
    url(r'^focus/location/create/$', views.LocationCreateView.as_view(), name='focus_location_create'),
    url(r'^focus/location/detail/(?P<slug>\S+)/$', views.LocationDetailView.as_view(), name='focus_location_detail'),
    url(r'^focus/location/update/(?P<slug>\S+)/$', views.LocationUpdateView.as_view(), name='focus_location_update'),
)

