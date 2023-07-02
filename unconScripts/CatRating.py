import random

def get_pos():
    num = random.randint(1,5)

    if(num == 1):
        pos = "pg"
        return pos
    elif(num == 2):
        pos = "sg"
        return pos
    elif(num == 3):
        pos = "sf"
        return pos
    elif(num == 4):
        pos = "pf"
        return pos
    elif(num == 5):
        pos = "c"
        return pos
    
# -shooter
#     -3pt
#     -mid
#     -standshot
#     -moveshot
# -playmaker
#     -passing accuracy
#     -dribbling
#     -dot(dimer)
# slashing
#     -drive
#     -dunk
#     -layup
# post
#     -backdown
#     -postmove
#     -close shot
#     -oBoard
#     -dBoard
# defense  
#     -perimeter defense
#     -post defense
#     -intimidation
#     -steal
#     -block
#     -reconition
# physical
#     -speed
#     -strength
#     -vertical


def scale():
    potScale = [1, 2, 3, 4, 5] #love me some pot.....scale
    weight = [.2, .3, .3, .15, .05]

    # scaleList = [.0, .0, .0, .0, .0, .0, .0, .0, .0]
    scale = random.choices(potScale, weights=weight, k=1)
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

    value = random.choice(nums, weights=weights, k=1)
    randNum = random.randint(1,9)
    rating = str(value) + str(randNum)
    return rating

def getOverall(three, mid, standShot, moveShot, passAcc, dribble, dot, drive, dunk, layup, backdown, postMove, closeShot, oBoard, dBoard, perDefense, postDefense, intimidation, steal, block, reconition, speed, strength, vertical):
    num = three + mid + standShot + moveShot + passAcc + dribble + dot + drive + dunk + layup + backdown + postMove + closeShot + oBoard + dBoard + perDefense + postDefense + intimidation + steal + block + reconition + speed + strength + vertical
    ovr = num/24
    return ovr

def main():
    shooter = scale()
    three = attribute(shooter)
    mid = attribute(shooter)
    standShot = attribute(shooter)
    moveShot = attribute(shooter)

    playmaker = scale()
    passAcc = attribute(playmaker)
    dribble = attribute(playmaker)
    dot = attribute(playmaker)

    slashing = scale()
    drive = attribute(slashing)
    dunk = attribute(slashing)
    layup = attribute(slashing)

    post = scale()
    backdown = attribute(post)
    postMove = attribute(post)
    closeShot = attribute(post)
    oBoard = attribute(post)
    dBoard = attribute(post)

    defense = scale()
    perDefense = attribute(defense)
    postDefense = attribute(defense)
    intimidation = attribute(defense)
    steal = attribute(defense)
    block = attribute(defense)
    reconition = attribute(defense)
    
    physical = scale()
    speed = attribute(physical)
    strength = attribute(physical)
    vertical = attribute(physical)

    ovr = getOverall(three, mid, standShot, moveShot, passAcc, dribble, dot, drive, dunk, layup, backdown, postMove, closeShot, oBoard, dBoard, perDefense, postDefense, intimidation, steal, block, reconition, speed, strength, vertical)

# -shooter
#     -3pt
#     -mid
#     -standshot
#     -moveshot
# -playmaker
#     -passing accuracy
#     -dribbling
#     -dot(dimer)
# slashing
#     -drive
#     -dunk
#     -layup
# post
#     -backdown
#     -postmove
#     -close shot
#     -oBoard
#     -dBoard
# defense  
#     -perimeter defense
#     -post defense
#     -intimidation
#     -steal
#     -block
#     -reconition
# physical
#     -speed
#     -strength
#     -vertical