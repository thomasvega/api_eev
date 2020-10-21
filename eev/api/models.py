from django.contrib.auth.models import User, Group
from django.db import models

# Create your models here.
class Module(models.Model):
    MODULES = (
        ('Picture', 'Picture'),
        ('CarPooling', 'CarPooling'),
        ('Music', 'Music'),
        ('TriCount', 'TriCount'),
        ('Poll', 'Poll'),
    )
    name = models.CharField(max_length=10, choices=MODULES)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=250)
    datetime_start = models.DateTimeField()
    datetime_end = models.DateTimeField()
    users = models.ManyToManyField(User, through='Guest')
    modules = models.ManyToManyField(Module, related_name='Modules')

    def __str__(self):
        return self.title

class Guest(models.Model):
    creator = models.BooleanField("Creator of the event")
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together= ('event', 'user')

    def __str__(self):
        return f'{self.event.title} has {self.user.username} as participant'


class Poll(models.Model):
    question = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)

    def __str__(self):
        return self.choice_text


class Vote(models.Model):
    choice = models.ForeignKey(Choice, related_name='votes', on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    voted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together= ('poll', 'voted_by')

# class Picture(models.Model):
#     name = models.CharField(max_length=200)
#     url = models.CharField(max_length=200)
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

# class Ride(models.Model):
#     address_start = models.CharField(max_length=200)
#     address_end = models.CharField(max_length=200)
#     datetime_start = models.DateTimeField()
#     datetime_end = models.DateTimeField()


# class CarPooling(models.Model):
#     driver = models.BooleanField('Driver', False)
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     ride = models.ForeignKey(Ride, on_delete=models.CASCADE)

#     def __str__(self):
#         if self.driver:
#             res = f'User {self.user.first_name} will drive'
#         else:
#             res = f'User {self.user.first_name} will be passenger'
#         return res