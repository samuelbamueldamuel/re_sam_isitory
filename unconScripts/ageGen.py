import random

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
list = []
for i in range(1000):
    list.append(getAge())

average = sum(list) / len(list)
print(average)

