from rest_framework import serializers

from django.contrib.auth.models import User, Group

from django.utils import timezone

from rest_framework.authtoken.models import Token

from .models import Module, Event, Guest, Poll, Choice, Vote

    
class VoteSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if data['user']:
            raise serializers.ValidationError("Il semblerait que vous avez déjà voté")
        return data

    class Meta:
        model = Vote
        fields = '__all__'

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Poll
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only':True}}
    
    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            username=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True)
    # user_list = ModuleSerializer(many=True, source='users')

    class Meta:
        model = Event
        fields = '__all__'


class GuestSerializer(serializers.ModelSerializer):
    event = EventSerializer()
    user = UserSerializer()

    class Meta:
        model = Guest
        fields = '__all__'