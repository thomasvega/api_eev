from rest_framework import serializers

from django.contrib.auth.models import User, Group

from django.utils import timezone

from rest_framework.authtoken.models import Token

from .models import Event, Participate, Poll, Choice, Vote


class EventSerializer(serializers.ModelSerializer):
    users = serializers.SlugRelatedField(
        many=True, 
        read_only=True,
        slug_field='first_name'
    )
    modules = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

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
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only':True}}
    
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user