from api.models import Event, Participate
from api.serializers import EventSerializer, ParticipateSerializer
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User, Group

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

class ParticipateCreate(generics.ListCreateAPIView):
    """
    Create new participation
    """
    queryset = Participate.objects.all()
    serializer_class = ParticipateSerializer

class ParticipateDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete participant in an event
    """
    def retrieve(self, request, pk):
        """
        Overiding retrieve method to get participating people from a particular event
        """
        queryset = Participate.objects.filter(event=pk).all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    queryset = Participate.objects.all()
    serializer_class = ParticipateSerializer