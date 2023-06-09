from django.urls import path
from . import views

# app_name = 'league'

urlpatterns = [
    path('players/', views.player, name='players'),
    path('do_shit/', views.do_shit, name = 'do_shit'),
    path('table/', views.table, name='table'),
    path('sdraft/', views.sdraft, name='draft'),
    path('ssdraft/', views.ssdraft, name='ssdraft')
]