from django.urls import path, include

from rest_framework.routers import DefaultRouter

from rest_framework import permissions

from .apiviews import GuestList, EventViewSet, PollViewSet, ChoiceList, CreateVote, UserCreate, LoginView, GuestRetrieveDestroy

router = DefaultRouter()
router.register('polls', PollViewSet, basename="polls")
router.register('events', EventViewSet, basename="events")

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('users/', UserCreate.as_view(), name="user_create"),
    path('polls/<int:pk>/choices/', ChoiceList.as_view(), name="choice_list"),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/', CreateVote.as_view(), name='create_vote'),
    path('events/<int:event_pk>/guests/', GuestList.as_view(), name="guest_list"),
    path('events/<int:event_pk>/guests/<int:guest_pk>', GuestRetrieveDestroy.as_view(), name="gest_retrieve_destroy"),
]

urlpatterns += router.urls