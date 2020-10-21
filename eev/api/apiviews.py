"""
Rule of Thumb :
- Use viewsets.ModelViewSet when you are going
to allow all or most of CRUD operations on a model
- Use generics.* when you only want to allow some
operations on a model
- use APIView when you want to completely customize the behaviour
"""

from rest_framework import generics

from rest_framework import status

from rest_framework import viewsets

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.exceptions import PermissionDenied, NotFound

from django.contrib.auth import authenticate

from django.utils import timezone

from datetime import datetime

from .serializers import GuestSerializer, EventSerializer, PollSerializer, ChoiceSerializer, VoteSerializer, UserSerializer

from .models import Event, Poll, Choice, Vote, Guest

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def check_date(self, start, end):
        """
        Comparing dates
        """
        FORMAT_DATE = '%Y-%m-%dT%H:%M'
        if not datetime.strptime(start, FORMAT_DATE) > datetime.now():
            raise PermissionDenied('You can not have the starting date inferior to todays date')
        if not datetime.strptime(end, FORMAT_DATE) > datetime.strptime(start, FORMAT_DATE):
            raise PermissionDenied('Ending date must be superior to starting date')
    
    def check_creator(self, event_id, request):
        """
        Looking if the request user is the creator of the event
        """
        event = Event.objects.get(pk=event_id)
        try:
            creator = Guest.objects.get(creator=True, event=event, user=request.user.id)
        except Guest.DoesNotExist:
            creator = None

        if not request.user == creator:
            raise PermissionDenied('You can not delete this event.')

    def create(self, request, *args, **kwargs):
        """
        Ensure the event will be created only if 
        the end date is superior to start date
        and if the start date is superior to today's
        """
        self.check_date(request.data['datetime_start'], request.data['datetime_end'])
        data = {
            'title': request.data.get('title'), 
            'description': request.data.get('description'), 
            'datetime_start': request.data.get('datetime_start'), 
            'datetime_end': request.data.get('datetime_end'), 
            'modules': [request.data.get('modules')]
        }
        serializer = EventSerializer(data=data)
        if serializer.is_valid():
            event = serializer.save()
            participate = Guest(creator=True, event=event, user=request.user)
            participate.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, *args, **kwargs):
        """
        Ensure the event will be updated only if the end date is superior to start date
        and if the start date is superior to today's date
        """
        self.check_date(request.data['datetime_start'], request.data['datetime_end'])
        self.check_creator(self.kwargs['pk'], request)
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        """
        Ensure the event can only be deleted by the one who created it
        """
        self.check_creator(self.kwargs['pk'], request)
        return super().destroy(request, *args, **kwargs)


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def destroy(self, request, *args, **kwargs):
        """
        Overriding destroy method to make sure it's only the user
        who created the poll that is able to delete it
        """
        poll = Poll.objects.get(pk=self.kwargs['pk'])
        if not request.user == poll.created_by:
            raise PermissionDenied('You can not delete this poll.')
        return super().destroy(request, *args, **kwargs)


class ChoiceList(generics.ListCreateAPIView):
    serializer_class = ChoiceSerializer

    def get_queryset(self):
        queryset = Choice.objects.filter(poll_id=self.kwargs['pk'])
        return queryset
    
    def post(self, request, *args, **kwargs):
        """
        Overriding post method to make sure it's only the
        user who created the poll that is able to add choice
        """
        poll = Poll.objects.get(pk=self.kwargs['pk'])
        if not request.user == poll.created_by:
            raise PermissionDenied('You can not create choice for this poll.')
        return super().post(request, *args, **kwargs)


class CreateVote(APIView):

    def post(self, request, pk, choice_pk):
        voted_by = request.data.get("voted_by")
        data = {'choice': choice_pk, 'poll': pk, 'voted_by': voted_by}
        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GuestList(generics.ListCreateAPIView):
    serializer_class = GuestSerializer

    def get_queryset(self):
        """
        Retrieving all guests from an event id
        """
        queryset = Guest.objects.filter(event_id=self.kwargs['event_pk'])
        return queryset
    

class GuestRetrieveDestroy(generics.RetrieveDestroyAPIView):
    serializer_class = GuestSerializer

    def get_object(self):
        """
        Retrieving a specific guest
        """
        try:
            guest = Guest.objects.get(pk=self.kwargs['guest_pk'])
        except Guest.DoesNotExist:
            raise NotFound("The item you're searching for doesn't exist.")
        return guest
        
    def destroy(self, request, *args, **kwargs):
        """
        Overriding destroy method so it is possible to delete only if you are the creator 
        or if it yourself
        """
        guest_list = Guest.objects.filter(pk=self.kwargs['event_pk'])
        for guest in guest_list:
            if not request.user == guest.creator or request.user == guest.user:
                raise PermissionDenied("You can not delete this poll.")
        return super().destroy(request, *args, **kwargs)
        

class UserCreate(generics.CreateAPIView):
    """
    Giving exemption to UserCreate view for authentication by
    overriding the global setting.
    authentication_classes = () 
    and
    permission_classes = () will do the job
    """
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request, ):
        username= request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({'token': user.auth_token.key})
        else:
            return Response({'error': 'Wrong Credentials'}, status=status.HTTP_400_BAD_REQUEST)