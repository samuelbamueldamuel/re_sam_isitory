from django.core.management.base import BaseCommand, CommandParser
from league.models import FName, LName
import random

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for i in range(100):
            num = random.randint(1, 1000)
            # num = 405
            obj = LName.objects.filter(id=num).first()
            if obj == None:
                print(str(num) + " is null")
            else:
                lname = obj.lastName
                print("num is: " +  str(num) + "name: " + lname)
            # if lname != None:
            #     print("num is: " +  str(num) + "name: " + lname)
            # else: 
            #     print(str(num) + " is null")