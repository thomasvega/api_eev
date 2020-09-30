from api.models import Event
from api.serializers import EventSerializer

from rest_framework import generics

class EventList(generics.ListCreateAPIView):
    """
    List all the event or create a new event.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an event.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer