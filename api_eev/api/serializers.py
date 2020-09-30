from rest_framework import serializers
from django.contrib.auth.models import User, Group

from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'email']

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['name']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['title', 'description', 'datetime_start', 'datetime_end', 'users', 'modules']

class ParticipateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participate
        fields = ['creator', 'event', 'user']

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question

class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice

class VoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vote

class PictureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Picture

class RideSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ride

class CarPoolingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarPooling