from django.db import models

class Team(models.Model):
    city = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    t_id = models.CharField(max_length=5, primary_key=True)
    conference = models.CharField(max_length=4, null=True)
    division = models.CharField(max_length=10, null=True)
    userTeam = models.BooleanField(default=False)
    sixTeams = models.IntegerField(default=0)
    fourTeams = models.IntegerField(default=0)



class Player(models.Model):
    team = models.ForeignKey(Team, null=False, default='FAA', on_delete=models.CASCADE)
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


    
    age = models.IntegerField(null=True)
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

    shooter = models.IntegerField()

    playmaker = models.IntegerField()

    slashing = models.IntegerField()

    post = models.IntegerField()

    defense = models.IntegerField()

    physical = models.IntegerField()

    value = models.IntegerField(null=True)
    salary = models.FloatField(null=True)



class FName(models.Model):
    firstName = models.CharField(max_length=55)

class LName(models.Model):
    lastName = models.CharField(max_length=55)
        
class Offer(models.Model):
    team_name = models.CharField(max_length=100)
    offer = models.DecimalField(max_digits=6, decimal_places=2)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.team_name}: {self.offer}"

class Game(models.Model):
    homeTeam = models.ForeignKey(Team, related_name='home_games', null=True, on_delete=models.CASCADE)
    awayTeam = models.ForeignKey(Team, related_name='away_games', null=True, on_delete=models.CASCADE)

    
    week = models.IntegerField()


# Create your models here.
