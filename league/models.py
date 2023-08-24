from django.db import models

class Team(models.Model):
    city = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    t_id = models.CharField(max_length=5, primary_key=True)
    conference = models.CharField(max_length=4, null=True)
    division = models.CharField(max_length=10, null=True)
    userTeam = models.BooleanField(default=False)




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

    winner = models.ForeignKey(Team, related_name='winner', null=True, on_delete=models.CASCADE)
    loser = models.ForeignKey(Team, related_name='loser', null=True, on_delete=models.CASCADE)


class Record(models.Model):
    team = models.OneToOneField(Team, related_name='record', null=False, on_delete=models.CASCADE)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)

class Time(models.Model):
    stages = (
        ('reg', 'Regular Season'),
        ('playoffs', 'Playoffs'),
        ('draft', 'Draft'),
        ('free', 'Free Agency'),
    )

    stage = models.CharField(max_length=15, choices=stages, default='reg')
    week = models.IntegerField()

class PlayoffGame(models.Model):
    rounds = (
        ('first', 'First Round'),
        ('second', 'Second Round'),
        ('semis', 'Conference Finals'),
        ('finals', 'Finals'),
    )

    round = models.CharField(max_length=25, choices=rounds, null=True)

    homeTeam = models.ForeignKey(Team, related_name='playoffHome', null=False, on_delete=models.CASCADE)
    awayTeam = models.ForeignKey(Team, related_name='playoffAway', null=False, on_delete=models.CASCADE)

    winner = models.ForeignKey(Team, related_name='playoffWinner', null=True, on_delete=models.CASCADE)
    loser = models.ForeignKey(Team, related_name='playoffLoser', null=True, on_delete=models.CASCADE)
    conference = models.CharField(max_length=5, null=True)

class PlayoffTeam(models.Model):
    seed = models.IntegerField()
    team = models.ForeignKey(Team, related_name='playoffTeam', null=True, on_delete=models.CASCADE)
    conference = models.CharField(max_length=5, null=True)
class Draft(models.Model):
    pick = models.IntegerField()
    team = models.ForeignKey(Team, related_name='draft', on_delete=models.CASCADE)
    player = models.ForeignKey(Player, related_name='pick', null=True, on_delete=models.CASCADE)
    userPick = models.BooleanField(default=False)
class CurrentPick(models.Model):
    pick = models.IntegerField()





# Create your models here.
