from django.urls import path
from league.views import AdminViews, UserViews

# app_name = 'league'

urlpatterns = [
    path('players/', AdminViews.player, name='players'),
    path('do_shit/', AdminViews.do_shit, name = 'do_shit'),
    path('table/', AdminViews.table, name='table'),
    path('sdraft/', AdminViews.sdraft, name='draft'),
    path('ssdraft/', AdminViews.ssdraft, name='ssdraft'),
    path('<str:t_id>/roster', AdminViews.roster, name='roster'),
    path('index/', AdminViews.index, name='index'),
    path('delete/', AdminViews.deletePlay, name='delete'),
    path('welcome/', UserViews.welcome, name='welcome'),
    path('makeUserTeam/<str:t_id>', AdminViews.makeUserTeam, name='makeUserTeam'),
    path('testSelTeam/', AdminViews.testSelTeam, name='testSelTeam'),
    path('home/', UserViews.home, name='home'),
    path('teamRoster/', UserViews.teamRoster, name='teamRoster'),
    path('teams/', UserViews.teams, name='teams'),
    path('playerPage/<str:id>', UserViews.playerPage, name='playerPage'),
    path('assignSalary', AdminViews.assignSalary, name='assignSalary'),
    path('salaryBreakdown/', UserViews.salaryBreakdown, name='salaryBreakdown'),
    path('leagueSalary/', UserViews.leagueSalary, name='leagueSalary'),
    path('testView/', UserViews.testView, name='testView'),
    path('salaryBreakdownL/<str:t_id>', UserViews.salaryBreakdownL, name='salaryBreakdownL'),
    path('makeSched', AdminViews.makeSched, name='makeSched'),
    path('teamGames', UserViews.teamGames, name='teamGames'),
    path('leagueGames/<str:week>', UserViews.leagueGames, name='leagueGames'),
    path('leagueGame', UserViews.leagueGame, name='leagueGame'),
    path('simSeason', AdminViews.simSeason, name='simSeason'),
    path('standings', UserViews.standings, name='standings'),
]