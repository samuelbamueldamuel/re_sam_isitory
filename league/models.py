from django.db import models

class Team(models.Model):
    city = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    t_id = models.CharField(max_length=5, primary_key=True)


class Player(models.Model):
    team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    pos = models.CharField(max_length=2)
    height = models.CharField(max_length=10)
    weight = models.IntegerField()

    ovr = models.IntegerField()

    three = models.IntegerField()
    mid = models.IntegerField()
    standShot = models.IntegerField()
    moveShot = models.IntegerField()
    passAcc = models.IntegerField()
    dribble = models.IntegerField()
    dot = models.IntegerField()
    drive = models.IntegerField()
    dunk = models.IntegerField()
    layup = models.IntegerField()
    backdown = models.IntegerField()
    postMove = models.IntegerField()
    closeShot = models.IntegerField()
    oBoard = models.IntegerField()
    dBoard = models.IntegerField()
    perDefense = models.IntegerField()
    postDefense = models.IntegerField()
    intimidation = models.IntegerField()
    steal = models.IntegerField()
    block = models.IntegerField()
    reconition = models.IntegerField()
    speed = models.IntegerField()
    strength = models.IntegerField()
    vertical = models.IntegerField()

class FName(models.Model):
    firstName = models.CharField(max_length=55)

class LName(models.Model):
    lastName = models.CharField(max_length=55)


# Create your models here.
