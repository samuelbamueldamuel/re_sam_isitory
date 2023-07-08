import random 
import numpy
from ageGen import getAge
def scale():
    potScale = [1, 2, 3, 4, 5] #love me some pot.....scale
    weight = [.2, .3, .3, .15, .05]

    # scaleList = [.0, .0, .0, .0, .0, .0, .0, .0, .0]
    scaleL = random.choices(potScale, weights=weight, k=1)
    scale = scaleL[0]
    if(scale == 1):
        scaleList = [.3, .3, .2, .1, .1, 0, 0, 0, 0]
    elif(scale == 2):
        scaleList = [.1, .3, .2, .2, .1, .1, .0, .0, .0]
    elif(scale == 3):
        scaleList = [.0, .0, .1, .3, .3, .2, .1, .0, .0]
    elif(scale == 4):
        scaleList = [.0, .0, .0, .0, .3, .3, .2, .15, .05]
    elif(scale == 5):
        scaleList = [.0, .0, .0, .0, .1, .3, .3, .2, .1]

    return scaleList

def attribute(weights):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    valueL = random.choices(nums, weights=weights, k=1)
    value = valueL[0]
    randNum = random.randint(1,9)
    ratingL = str(value) + str(randNum)
    rating = int(ratingL)

    return rating

def getOverall(three, mid, standShot, moveShot, passAcc, dribble, dot, drive, dunk, layup, backdown, postMove, closeShot, oBoard, dBoard, perDefense, postDefense, intimidation, steal, block, reconition, speed, strength, vertical):
    
    num = int(three) + int(mid)+ int(standShot) + int(moveShot) + int(passAcc) + int(dribble) + int(dot) + int(drive) + int(dunk) + int(layup) + int(backdown) + int(postMove) + int(closeShot) + int(oBoard) + int(dBoard) + int(perDefense) + int(postDefense) + int(intimidation) + int(steal) + int(block) + int(reconition) + int(speed) + int(strength) + int(vertical)
    ovr = num/24
    return ovr

def shooterF(three, mid, standShot, moveShot):
    average = (int(three) + int(mid) + int(standShot) + int(moveShot)) / 4
    return round(average)

def playmakerF(passAcc, dribble, dot):
    average = (int(passAcc) + int(dribble) + int(dot))/ 3
    return round(average)

def slashingF(drive, layup, dunk):
    average = (int(drive) + int(layup) + int(dunk)) / 3
    return round(average)

def postF(backdown, postMove, closeShot, oBoard, dBoard):
    average = (int(backdown) + int(postMove) + int(closeShot) + int(oBoard) + int(dBoard)) / 5
    return round(average)

def defenseF(perDefense, postDefense, intimidation, steal, block, reconition):
    average = (int(perDefense) + int(postDefense) + int(intimidation) + int(steal) + int(block) + int(reconition)) / 6
    return round(average)

def physicalF(speed, strength, vertical):
    average = (int(speed) + int(strength) + int(vertical)) / 3
    return round(average)

def ageFdig():
    weights = [5, 3]
    nums = [2, 3]

    dig = random.choices(nums, weights=weights)
    return dig

def ageLdig(firstDigit):
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    if(firstDigit == 2):
        weights = [1, 1, 2, 2, 3 , 3, 3, 3, 3, 3]
    elif(firstDigit == 3):
        weights = [5, 4, 3, 2, 1, 0.5, 0.5, 0.5, 0.5, 0.5]

    dig = random.choices(nums, weights=weights)
    return dig


def getAge():
    firstDigit = str(ageFdig())
    lastDigit = str(ageLdig(int(firstDigit[1])))

    ageString = firstDigit + lastDigit

    age = firstDigit[1] + lastDigit[1]
    return int(age)

def birth():
    shooter = scale()
    three = attribute(shooter)
    mid = attribute(shooter)
    standShot = attribute(shooter)
    moveShot = attribute(shooter)

    shooterA = shooterF(three, mid, standShot, moveShot)

    playmaker = scale()
    passAcc = attribute(playmaker)
    dribble = attribute(playmaker)
    dot = attribute(playmaker)

    playmakerA = playmakerF(passAcc, dribble, dot)

    slashing = scale()
    drive = attribute(slashing)
    dunk = attribute(slashing)
    layup = attribute(slashing)

    slashingA = slashingF(drive, dunk, layup)

    post = scale()
    backdown = attribute(post)
    postMove = attribute(post)
    closeShot = attribute(post)
    oBoard = attribute(post)
    dBoard = attribute(post)

    postA = postF(backdown, postMove, closeShot, oBoard, dBoard)

    defense = scale()
    perDefense = attribute(defense)
    postDefense = attribute(defense)
    intimidation = attribute(defense)
    steal = attribute(defense)
    block = attribute(defense)
    reconition = attribute(defense)

    defenseA = defenseF(perDefense, postDefense, intimidation, steal, block, reconition)
    
    physical = scale()
    speed = attribute(physical)
    strength = attribute(physical)
    vertical = attribute(physical)

    physicalA = physicalF(speed, strength, vertical)

    

    ovr = getOverall(three, mid, standShot, moveShot, passAcc, dribble, dot, drive, dunk, layup, backdown, postMove, closeShot, oBoard, dBoard, perDefense, postDefense, intimidation, steal, block, reconition, speed, strength, vertical)

    return ovr

def ranOvr():
    ovr = random.randint(20,70)
    return ovr
def ranAge():
    age = random.randint(20,38)
    return age

def val(ovr, age):

    ovrVal = int(ovr) * 4
    ageVal = int(age) * 2

    val = ovrVal - ageVal
    return val

def main():
    age = getAge()
    ovr = birth()

    value = val(ovr, age)
    print("Overall: " + str(ovr) + "Age: " + str(age) + "val:" + str(value) )
    return value


list = []
for i in range(10000):
   value =  main()
   list.append(value)

average = sum(list) / len(list)
std = numpy.std(list)

firQuar = numpy.percentile(list, 25)
thirQuar = numpy.percentile(list, 75)

percentiles = {
    "p10": numpy.percentile(list, 10),
    "p20": numpy.percentile(list, 20),
    "p30": numpy.percentile(list, 30),
    "p40": numpy.percentile(list, 40),
    "p50": numpy.percentile(list, 50),
    "p60": numpy.percentile(list, 60),
    "p70": numpy.percentile(list, 70),
    "p80": numpy.percentile(list, 80),
    "p90": numpy.percentile(list, 90),
    "p100": numpy.percentile(list, 100)
}

print("avg: "  + str(average))
print("std: " + str(std))
print("q1: " + str(firQuar))
print("q3: " + str(thirQuar))
print("10% percentile:", percentiles["p10"])
print("20% percentile:", percentiles["p20"])
print("30% percentile:", percentiles["p30"])
print("40% percentile:", percentiles["p40"])
print("50% percentile:", percentiles["p50"])
print("60% percentile:", percentiles["p60"])
print("70% percentile:", percentiles["p70"])
print("80% percentile:", percentiles["p80"])
print("90% percentile:", percentiles["p90"])
print("100% percentile:", percentiles["p100"])

