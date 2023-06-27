from django.db import models

class Team(models.Model):
    city = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    t_id = models.CharField(max_length=3, primary_key=True)


class Player(models.Model):
    team = models.ForeignKey(to=Team, on_delete=models.CASCADE, null=True, default='FA', related_name='players')
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    pos = models.CharField(max_length=2)
    height = models.CharField(max_length=10)
    ovr = models.IntegerField()
    three = models.IntegerField()
    mid = models.IntegerField()
    close = models.IntegerField()
    dribble = models.IntegerField()
    passing = models.IntegerField()
    perimeter_defense = models.IntegerField()
    post_defense = models.IntegerField()
    steal = models.IntegerField()
    block = models.IntegerField()
    test = models.IntegerField(default='1')

class FName(models.Model):
    firstName = models.CharField(max_length=55)

class LName(models.Model):
    lastName = models.CharField(max_length=55)


# Create your models here.
