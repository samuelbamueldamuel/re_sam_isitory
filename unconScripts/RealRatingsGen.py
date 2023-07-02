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

#from league.models import FName, LName
import random

def getFName():
    num = random.randint(1,1000)
    firstName = FName.objects.get(id=num)
    return firstName

def getLName():
    num = random.randint(1,1000)
    lastName = LName.objects.get(id=num)
    return lastName

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

def get_height(pos): # i hate my life why did I do this to myself holy shit WHAT WAS I SMOKING 
    #words can not express how much I hate myself for writing this function like this but Im too lazy to do it again 
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

def thirdDig():
        nums = [0,1,2,3,4,5,6,7,8,9]
        w = [1,1,1,1,1,1,1,1,1,1]
        td = random.choices(population=nums, weights=w, k=1)
        return td






def ranH(heights, weights): #pretty sure its useless but dont wanna delete anything
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

def birth():
    firstName = "joe"
    lastName = "schmoe"
    pos = get_pos()
    height = str(get_height(pos))
    weight = weight_func(height)
    print("pos:" + pos)
    print("height:" + height)
    print("weight:" + weight)



for i in range(5):
    birth()

    

