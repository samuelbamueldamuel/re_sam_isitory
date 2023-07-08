from league.models import Player
import random
def getSalary(value):
    value = int(value)

    if(value >= 210):
        values = [35, 36, 37, 38, 39, 40]
        weight = [1, 1, 1, 1, 1, 1]
    elif(190 <= value < 210 ):
        values = [30, 31, 32, 33, 34, 35]
        weight = [1, 1, 1, 1, 1, 1]
    elif(160 <= value < 190 ):
        values = [24, 25,  26, 27, 28, 29]
        weight = [1, 1, 1, 1, 1, 1]
    elif(140 <= value < 160):
        values = [19, 20, 21, 22, 23]
        weight = [1, 1, 1, 1, 1]
    elif(150 <= value < 160):
        values = [12, 13, 14, 15, 16, 17, 18]
        weight = [1, 1, 1, 1, 1, 1, 1]
    elif(140 <= value < 150):
        values = [9, 10, 11]
        weight = [1, 1, 1]
    elif(100 <= value < 140):
        values = [7, 8, 9]
        weight = [1, 1, 1]
    elif(80 <= value < 100):
        values = [4, 5, 6]
        weight = [1, 1, 1]
    else:
        values = [0, 1, 2, 3]
        weight = [1, 1, 1, 1]

    firstDigit = random.choices(values, weights=weight)
    firstDigit = str(firstDigit[0])
    
    lastDigit = random.randint(0, 9)
    lastDigit = str(lastDigit)

    salary = firstDigit + "." + lastDigit
    salary = float(salary)
    return salary

    


    
def main():
    players = Player.objects.order_by('id')

    for player in players:
        salaryVar = getSalary(player.value)
        player.salary = salaryVar
        player.save()


