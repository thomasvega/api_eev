from django.contrib import admin

# Register your models here.
from .models import Event, Guest, Module, Poll, Choice, Vote
#  Module, Guest, Poll, PollOption, Media, TypeMedia, Supply, CarPooling, Ride


admin.site.register(Event)
admin.site.register(Guest)
admin.site.register(Module)
admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Vote)