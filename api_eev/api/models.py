from django.contrib.auth.models import User, Group
from django.db import models

# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.first_name

class Module(models.Model):
    MODULES = (
        ('Picture', 'Picture'),
        ('CarPooling', 'CarPooling'),
        ('Music', 'Music'),
        ('TriCount', 'TriCount'),
        ('Poll', 'Poll'),
    )
    name = models.CharField(max_length=25, choices=MODULES)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    datetime_start = models.DateTimeField()
    datetime_end = models.DateTimeField()
    members = models.ManyToManyField(Member, through='Participate')
    modules = models.ManyToManyField(Module)

    def __str__(self):
        return self.title

class Participate(models.Model):
    creator = models.BooleanField(False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.choice_text
    
class Vote(models.Model):
    vote = models.BooleanField('Vote', False)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return f'User {self.member.user.first_name} voted {self.vote}'

class Picture(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Ride(models.Model):
    address_start = models.CharField(max_length=200)
    address_end = models.CharField(max_length=200)
    datetime_start = models.DateTimeField()
    datetime_end = models.DateTimeField()


class CarPooling(models.Model):
    driver = models.BooleanField('Driver', False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)

    def __str__(self):
        if self.driver:
            res = f'User {self.member.user.first_name} will drive'
        else:
            res = f'User {self.member.user.first_name} will be passenger'
        return res