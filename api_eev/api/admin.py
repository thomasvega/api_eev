from django.contrib import admin

# Register your models here.
from .models import Event, Participate, Module, Question, Choice, Vote, Picture, Ride, CarPooling
#  Module, Participate, Poll, PollOption, Media, TypeMedia, Supply, CarPooling, Ride


admin.site.register(Event)
admin.site.register(Participate)
admin.site.register(Module)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Vote)
admin.site.register(Picture)
admin.site.register(Ride)
admin.site.register(CarPooling)