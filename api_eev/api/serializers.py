from rest_framework import serializers
from django.contrib.auth.models import User, Group
from django.utils import timezone

from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'email']

class EventSerializer(serializers.ModelSerializer):
    def validate(self, data):
        """
        Check that the end if after the start.
        """
        if data['datetime_start'] < timezone.now():
            raise serializers.ValidationError("La date de début ne peux pas être antérieur à la date du jour")
        if data['datetime_end'] < data['datetime_start']:
            raise serializers.ValidationError("La date de fin doit être après la date de début")
        return data

    class Meta:
        model = Event
        fields = ['title', 'description', 'datetime_start', 'datetime_end', 'users', 'modules']

class ParticipateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participate
        fields = ['creator', 'event', 'user']
