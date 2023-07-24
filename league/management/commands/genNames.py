from django.core.management.base import BaseCommand, CommandParser
from league.models import FName, LName
import requests

class Command(BaseCommand):
    help = "pulls from name api and adds them to model"
    def getFName(self):
        url = "https://api.namefake.com/"
        response = requests.get(url).json()

        initName = response['name'].split()[0]

        if (initName == 'Mr.' or initName == 'Dr.' or initName == 'Mrs.' or initName == 'Ms.' or initName == 'Miss' or initName == 'Prof.'):
            name = response['name'].split()[1]
        else:
            name = response['name'].split()[0]

        
        return name
    def pushFName(self, name ):
        instance = FName(firstName=name)
        instance.save()

    def getLName(self):
        url = "https://api.namefake.com/"
        response = requests.get(url).json()

        initName = response['name'].split()[0]

        if (initName == 'Mr.' or initName == 'Dr.' or initName == 'Mrs.' or initName == 'Ms.' or initName == 'Miss' or initName == 'Prof.'):
            name = response['name'].split()[2]
        else:
            name = response['name'].split()[1] 
        return name  

    def pushLName(self, name):
           instance = LName(lastName=name)
           instance.save()

    def add_arguments(self, parser):
        parser.add_argument('num', type=int, help='num of names to be added')
        parser.add_argument('word', type=str, help='test word')

    def handle(self, *args, **kwargs):
        num = kwargs['num']
        word = kwargs['word']
        print(word)
        f = 1
        l = 1
        # for i in range(num):
        #     FName = self.getFName()
        #     self.pushFName(FName)
        #     print(f)
        #     f += 1
            
        for i in range(num):
            LName = self.getLName()
            self.pushLName(LName)
            print(l)
            l += 1
        
        

