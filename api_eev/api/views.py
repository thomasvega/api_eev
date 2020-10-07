from api.models import Event, Participate, Question, Choice, Vote
from api.serializers import EventSerializer, ParticipateSerializer, QuestionSerializer, ChoiceSerializer, VoteSerializer
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

class QuestionListCreate(generics.ListCreateAPIView):
    """
    List and create new question
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete question for an event
    """
    def retrieve(self, request, pk):
        """
        Overiding retrieve method to get question for an event
        """
        queryset = Question.objects.filter(event=pk).all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceListCreate(generics.ListCreateAPIView):
    """
    List and create new choice
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class ChoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete question for an event
    """
    def retrieve(self, request, pk):
        """
        Overiding retrieve method to get choice for a question
        """
        queryset = Choice.objects.filter(question=pk).all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class VoteListCreate(generics.ListCreateAPIView):
    """
    List and create new vote
    """
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

class VoteDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete vote for a choice
    """
    def retrieve(self, request, pk):
        """
        Overiding retrieve method to get choice for a specific choice
        """
        queryset = Vote.objects.filter(choice=pk).all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer