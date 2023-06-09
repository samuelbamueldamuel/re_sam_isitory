import random
from enum import Enum
from secrets import choice
from league.models import Player
import time
import requests



# ADD fname varchar(50), checl
# ADD lname varchar(50), check
# ADD team_id int, 
# add ovr int,
# add player_id int,
# ADD position varchar(2), check
# ADD height VARCHAR(8), check
# ADD three int,
# add mid int,
# add close int,
# add dribble int,
# add pass int,
# add perimeter_defense int,
# add post_defense int,
# add steal int,
# add block int;


# class position(Enum):
#     pg = 1;
#     sg = 2;
#     sf = 3;
#     pf = 4;
#     c = 5;






def get_fname():
    url = "https://api.namefake.com/"
    response = requests.get(url).json()
    initFName = response['name'].split()[0]
    if (initFName == 'Mr.' or initFName == 'Dr.' or initFName == 'Mrs.' or initFName == 'Ms.'):
        fname = response['name'].split()[2]
    else:
        fname = response['name'].split()[1]

    return fname    


def get_lname():
    url = "https://api.namefake.com/"
    response = requests.get(url).json()
    
    initFName = response['name'].split()[0]

    if (initFName == 'Mr.' or initFName == 'Dr.' or initFName == 'Mrs.' or initFName == 'Ms.'):
        lname = response['name'].split()[2]
    else:
        lname = response['name'].split()[1]
        

    return lname


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
    

def firstDig(pos):
 
    posX = str(pos)
    if(posX == "pg"):
        num = [5,6]
        weight = [.3, .7]
        dig = random.choices(num, cum_weights=weight)
        return dig 
    elif(posX == "sg"):
        num = [5,6]
        weight = [.1, .9]
        dig = random.choices(num, cum_weights=weight)
        return dig   
    elif(posX == "sf"):
        potDigs = [5, 6, 7]
        weight = [.05, .9, .05]
    elif(posX == "pf"):
        potDigs = [6, 7]
        weight = [.9, .1]
    elif(posX == "c"):
        potDigs = [6, 7]
        weight = [.7, .3]


    dig = random.choices(potDigs, weight)
    return dig
    


def guardFirstDig(pos):
    num = [5, 6]
    if(pos == "pg"):
        weight = [.3, .7]
        dig = random.choices(num, cum_weights=weight)
        return dig
    elif(pos == "sg"):
        weight = [.1, .9]
        dig = random.choices(num, cum_weights=weight)
        return dig

  

def gLDig(fDig):
    if(fDig == 6):
        potDigs = [0,1,2,3,4,5,6,7,8]
        weight = [9,8,7,6,5,4,3,2,1]
        dig = random.choices(potDigs, weights=weight)
        return dig
    elif(fDig == 5):
        potDigs = [8,9,10,11]
        weight = [1,2,3,4]
        dig = random.choices(potDigs, weights=weight)
        return dig
    else:
        return


def lastDig(posX, fDig):
    #print("pos: ", posX)
    #print("fDig: ", fDig)
    pos = str(posX)
    if(pos == "sf"):
        potDigs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        weight = [1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1]
        dig = random.choices(potDigs, weights=weight)
        return dig
    elif(pos == "pf"):
        if(fDig == 6):
            potDigs = [4, 5, 6, 7, 8, 9, 10, 11]
            weight = [.5, 1, 1, 2, 2, 3, 3, 2]
            dig = random.choices(potDigs, weights=weight)
            return dig
        elif(fDig == 7):
            potDigs = [0, 1, 2]
            weight = [3, 1, 1]
            dig = random.choices(potDigs, weights=weight)
            return dig
    elif(pos == "c"):
        if(fDig == 6):
            potDigs = [ 8, 9, 10, 11]
            weight = [1, 3, 3, 3]
            dig = random.choices(potDigs, weights=weight)
            return dig
        elif(fDig == 7):
            potDigs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
            weight = [3, 3, 3, 2, 1, 1, 1, .5, .5, .3, .2, .1]
            dig = random.choices(potDigs, weights=weight)
            return dig

def get_height(pos):
    
    if(pos == "pg"):
        ffDig = guardFirstDig(pos)
        #print("ffDig: ", ffDig)
        fDig = int(ffDig[0])
        flDig = gLDig(fDig)
        lDig = int(flDig[0])
        height = str(fDig) + "'" + str(lDig)
        return height
    elif(pos == "sg"):
        ffDig = guardFirstDig(pos) # first first 
        fDig = int(ffDig[0])
        flDig = gLDig(fDig) #first last digit code
        lDig = int(flDig[0])

        height = str(fDig) + "'" + str(lDig)
        return height
    else:
        ffDig = firstDig(pos)
        
        fDig = int(ffDig[0])
        print(fDig)
        flDig = lastDig(pos, fDig)
        print(flDig)
        print(pos)
        if isinstance(flDig, (str, int, float)):       #WTF IS THIS?????????????????? WHO LET ME COOK
            lDig = int(flDig) #might need to be accesses as a list
        elif isinstance(flDig, (list, tuple, dict)):
            lDig = int(flDig[0])
        else: 
            lDig = flDig[0]
        height = str(fDig) + "'" + str(lDig)
        
        return height
# test = get_pos()
# testtwo = get_height(position.sf)
# print(testtwo)
def thirdDig():
        nums = [0,1,2,3,4,5,6,7,8,9]
        w = [1,1,1,1,1,1,1,1,1,1]
        td = random.choices(population=nums, weights=w, k=1)
        return td






def ranH(heights, weights):
    ran = random.choices(population=heights, weights=weights, k=1)
    return ran[0]

def secondDig(fd):

    if(fd == 1):
        nums = [6,7,8,9]
        w = [1, 2, 2, 2]
    elif(fd == 2):
        nums = [0,1,2,3,4,5,6,7,8,9]
        w = [1,1,1,1,1,1,1,1,1,1]
    elif(fd == 3):
        nums = [0,1,2,3]
        w = [1,1,1,1]
    sd = random.choices(population=nums, weights=w, k=1)
    return sd



def seven():
    nums = [2, 3]
    w = [.9, .1] 

    fdString = random.choices(population=nums, weights=w, k=1)
    fd = int(fdString[0])
    return fd

def six(hLD):
    nums = [1, 2, 3]
    #print(hLD)
    if(hLD <= 2):
        w = [.2, .8, .0]
    elif(3 <= hLD <= 8 ):
        w = [.1, .9, .0]
    elif(hLD <= 9):
        w = [.0, .9, .1]
    elif(hLD >= 10):
        w = [.0, .8, .2]
    else:
        print("poopy")

    
    
    fdString = random.choices(population=nums, weights=w, k=1)
    fd = int(fdString[0])
    return fd
    

def five():
    nums = [1, 2]
    weights = [.8, .2]

    fdString = random.choices(population=nums, weights=weights, k=1)
    fd = int(fdString[0])
    return fd


def weight_func(h):
    
    hFDString = h[0] #height first digit
    if(len(h) >= 4): #appendages the last two digits of height #
        hLDString = str(h[2]) + str(h[3])
    else:
        hLDString = str(h[2])
    hFD = int(hFDString) # converty first digit to int
    hLD = int(hLDString)
    

    if(hFD == 5): #three funcs for different feet
        fdString = five()
    elif(hFD == 6):
        fdString = six(hLD)
    elif(hFD == 7):
        fdString= seven()
    else:
        fd = 2
        #print("accesed")
    
    fd = int(fdString)
    sd = secondDig(fd)
    td = thirdDig()

    weight = str(fd) + str(sd) + str(td)
    # print("Height is: " + str(h))
    # print("Weight is: " + str(weight))

    return weight
    

def randomRating():
    num = random.randint(1,99)
    return num
def ovr(three, mid, close, dribble, passing, perimeter_defense, post_defense, steal, block):
    total = three + mid + close + dribble + passing + perimeter_defense + post_defense + steal + block
    notRound = total/9
    ovr = round(notRound)
    return ovr

def birth():
    fName = str(get_fname())
    lName = str(get_lname())

    pos = get_pos()
    height = str(get_height(pos))
    weight = weight_func(height)
    three = randomRating()
    mid = randomRating()
    close = randomRating()
    dribble = randomRating()
    passing = randomRating()
    perimeter_defense = randomRating()
    post_defense = randomRating()
    steal = randomRating()
    block = randomRating()

    overall = ovr(three, mid, close, dribble, passing, perimeter_defense, post_defense, steal, block)

    # query = "INSERT INTO players (fname, lname, team_id, ovr, player_id, position, height, three, mid, close, dribble, passing, perimeter_defense, post_defense, steal, block) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    # cur = league.cursor()
    # cur.execute(query, (fName, lName, team_id, overall, player_id, pos, height, three, mid, close, dribble, passing, perimeter_defense, post_defense, steal, block))
    # league.commit()

    player = Player(
        first_name=fName,
        last_name=lName,
        pos=pos,
        height=height,
        ovr=overall,
        three=three,
        mid=mid,
        close=close,
        dribble=dribble,
        passing=passing,
        perimeter_defense=perimeter_defense,
        post_defense=post_defense,
        steal=steal,
        block=block,
        
    )
 
    player.save()


    # print("Player Statistics for", fName, lName)
    # print("Position:", pos)
    # print("Overall:", overall)
    # print("Height:", height, "inches")
    # print("Weight:", weight, "lbs")
    # print("Three-Point Rating:", three)
    # print("Mid-Range Rating:", mid)
    # print("Close-Range Rating:", close)
    # print("Dribble Rating:", dribble)
    # print("Passing Rating:", passing)
    # print("Perimeter Defense Rating:", perimeter_defense)
    # print("Post Defense Rating:", post_defense)
    # print("Steal Rating:", steal)
    # print("Block Rating:", block)
start = time.time()

end = time.time()
dur = end - start
print(dur)
# def test():
    # cur = league.cursor()
    # cur.execute("SELECT VERSION()")
    # result = cur.fetchone()
    # print("Database version:", result[0])
# test()