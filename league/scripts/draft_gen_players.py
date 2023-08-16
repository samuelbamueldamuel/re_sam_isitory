# import random
# from enum import Enum
# from secrets import choice
# from league.models import Player, FName, LName
# import time
# import requests








# def get_fname():
  

#     num = random.randint(1, 1000)
#     obj = FName.objects.values('firstName').filter(id=num).first()
    
    
#     fname = obj['firstName']


#     return fname


# def get_lname():
   

#     num = random.randint(1, 1000)
#     obj = LName.objects.values('lastName').filter(id=num).first()
    
    
#     lname = obj['lastName']

#     return lname


# def get_pos():
#     num = random.randint(1,5)

#     if(num == 1):
#         pos = "pg"
#         return pos
#     elif(num == 2):
#         pos = "sg"
#         return pos
#     elif(num == 3):
#         pos = "sf"
#         return pos
#     elif(num == 4):
#         pos = "pf"
#         return pos
#     elif(num == 5):
#         pos = "c"
#         return pos
    

# def firstDig(pos):
 
#     posX = str(pos)
#     if(posX == "pg"):
#         num = [5,6]
#         weight = [.3, .7]
#         dig = random.choices(num, cum_weights=weight)
#         return dig 
#     elif(posX == "sg"):
#         num = [5,6]
#         weight = [.1, .9]
#         dig = random.choices(num, cum_weights=weight)
#         return dig   
#     elif(posX == "sf"):
#         potDigs = [5, 6, 7]
#         weight = [.05, .9, .05]
#     elif(posX == "pf"):
#         potDigs = [6, 7]
#         weight = [.9, .1]
#     elif(posX == "c"):
#         potDigs = [6, 7]
#         weight = [.7, .3]


#     dig = random.choices(potDigs, weight)
#     return dig
    


# def guardFirstDig(pos):
#     num = [5, 6]
#     if(pos == "pg"):
#         weight = [.3, .7]
#         dig = random.choices(num, cum_weights=weight)
#         return dig
#     elif(pos == "sg"):
#         weight = [.1, .9]
#         dig = random.choices(num, cum_weights=weight)
#         return dig

  

# def gLDig(fDig):
#     if(fDig == 6):
#         potDigs = [0,1,2,3,4,5,6,7,8]
#         weight = [9,8,7,6,5,4,3,2,1]
#         dig = random.choices(potDigs, weights=weight)
#         return dig
#     elif(fDig == 5):
#         potDigs = [8,9,10,11]
#         weight = [1,2,3,4]
#         dig = random.choices(potDigs, weights=weight)
#         return dig
#     else:
#         return


# def lastDig(posX, fDig):
#     #print("pos: ", posX)
#     #print("fDig: ", fDig)
#     pos = str(posX)
#     if(pos == "sf"):
#         potDigs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#         weight = [1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1]
#         dig = random.choices(potDigs, weights=weight)
#         return dig
#     elif(pos == "pf"):
#         if(fDig == 6):
#             potDigs = [4, 5, 6, 7, 8, 9, 10, 11]
#             weight = [.5, 1, 1, 2, 2, 3, 3, 2]
#             dig = random.choices(potDigs, weights=weight)
#             return dig
#         elif(fDig == 7):
#             potDigs = [0, 1, 2]
#             weight = [3, 1, 1]
#             dig = random.choices(potDigs, weights=weight)
#             return dig
#     elif(pos == "c"):
#         if(fDig == 6):
#             potDigs = [ 8, 9, 10, 11]
#             weight = [1, 3, 3, 3]
#             dig = random.choices(potDigs, weights=weight)
#             return dig
#         elif(fDig == 7):
#             potDigs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#             weight = [3, 3, 3, 2, 1, 1, 1, .5, .5, .3, .2, .1]
#             dig = random.choices(potDigs, weights=weight)
#             return dig

# def get_height(pos): # i hate my life why did I do this to myself holy shit WHAT WAS I SMOKING 
#     #words can not express how much I hate myself for writing this function like this but Im too lazy to do it again 
#     if(pos == "pg"):
#         ffDig = guardFirstDig(pos)
#         #print("ffDig: ", ffDig)
#         fDig = int(ffDig[0])
#         flDig = gLDig(fDig)
#         lDig = int(flDig[0])
#         height = str(fDig) + "'" + str(lDig)
#         return height
#     elif(pos == "sg"):
#         ffDig = guardFirstDig(pos) # first first 
#         fDig = int(ffDig[0])
#         flDig = gLDig(fDig) #first last digit code
#         lDig = int(flDig[0])

#         height = str(fDig) + "'" + str(lDig)
#         return height
#     else:
#         ffDig = firstDig(pos)
        
#         fDig = int(ffDig[0])
#         print(fDig)
#         flDig = lastDig(pos, fDig)
#         print(flDig)
#         print(pos)
#         if isinstance(flDig, (str, int, float)):       #WTF IS THIS?????????????????? WHO LET ME COOK
#             lDig = int(flDig) #might need to be accesses as a list
#         elif isinstance(flDig, (list, tuple, dict)):
#             lDig = int(flDig[0])
#         else: 
#             lDig = flDig[0]
#         height = str(fDig) + "'" + str(lDig)
        
#         return height

# def thirdDig():
#         nums = [0,1,2,3,4,5,6,7,8,9]
#         w = [1,1,1,1,1,1,1,1,1,1]
#         td = random.choices(population=nums, weights=w, k=1)
#         return td






# def ranH(heights, weights): #pretty sure its useless but dont wanna delete anything
#     ran = random.choices(population=heights, weights=weights, k=1)
#     return ran[0]

# def secondDig(fd):

#     if(fd == 1):
#         nums = [6,7,8,9]
#         w = [1, 2, 2, 2]
#     elif(fd == 2):
#         nums = [0,1,2,3,4,5,6,7,8,9]
#         w = [1,1,1,1,1,1,1,1,1,1]
#     elif(fd == 3):
#         nums = [0,1,2,3]
#         w = [1,1,1,1]
#     sd = random.choices(population=nums, weights=w, k=1)
#     return sd



# def seven():
#     nums = [2, 3]
#     w = [.9, .1] 

#     fdString = random.choices(population=nums, weights=w, k=1)
#     fd = int(fdString[0])
#     return fd

# def six(hLD):
#     nums = [1, 2, 3]
#     #print(hLD)
#     if(hLD <= 2):
#         w = [.2, .8, .0]
#     elif(3 <= hLD <= 8 ):
#         w = [.1, .9, .0]
#     elif(hLD <= 9):
#         w = [.0, .9, .1]
#     elif(hLD >= 10):
#         w = [.0, .8, .2]
#     else:
#         print("poopy")

    
    
#     fdString = random.choices(population=nums, weights=w, k=1)
#     fd = int(fdString[0])
#     return fd
    

# def five():
#     nums = [1, 2]
#     weights = [.8, .2]

#     fdString = random.choices(population=nums, weights=weights, k=1)
#     fd = int(fdString[0])
#     return fd


# def weight_func(h):
    
#     hFDString = h[0] #height first digit
#     if(len(h) >= 4): #appendages the last two digits of height #
#         hLDString = str(h[2]) + str(h[3])
#     else:
#         hLDString = str(h[2])
#     hFD = int(hFDString) # converty first digit to int
#     hLD = int(hLDString)
    

#     if(hFD == 5): #three funcs for different feet
#         fdString = five()
#     elif(hFD == 6):
#         fdString = six(hLD)
#     elif(hFD == 7):
#         fdString= seven()
#     else:
#         fd = 2
#         #print("accesed")
    
#     fd = int(fdString)
#     sd = int(secondDig(fd)[0])
#     td = int(thirdDig()[0])

#     weightString = str(fd) + str(sd) + str(td)
#     weight = int(weightString)
    

#     return weight
    
# def scale():
#     potScale = [1, 2, 3, 4, 5] #love me some pot.....scale
#     weight = [.2, .3, .3, .15, .05]


#     scaleL = random.choices(potScale, weights=weight, k=1)
#     scale = scaleL[0]
#     if(scale == 1):
#         scaleList = [.3, .3, .2, .1, .1, 0, 0, 0, 0]
#     elif(scale == 2):
#         scaleList = [.1, .3, .2, .2, .1, .1, .0, .0, .0]
#     elif(scale == 3):
#         scaleList = [.0, .0, .1, .3, .3, .2, .1, .0, .0]
#     elif(scale == 4):
#         scaleList = [.0, .0, .0, .0, .3, .3, .2, .15, .05]
#     elif(scale == 5):
#         scaleList = [.0, .0, .0, .0, .1, .3, .3, .2, .1]

#     return scaleList

# def attribute(weights):
#     nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#     valueL = random.choices(nums, weights=weights, k=1)
#     value = valueL[0]
#     randNum = random.randint(1,9)
#     ratingL = str(value) + str(randNum)
#     rating = int(ratingL)

#     return rating

# def getOverall(three, mid, standShot, moveShot, passAcc, dribble, dot, drive, dunk, layup, backdown, postMove, closeShot, oBoard, dBoard, perDefense, postDefense, intimidation, steal, block, reconition, speed, strength, vertical):
    
#     num = int(three) + int(mid)+ int(standShot) + int(moveShot) + int(passAcc) + int(dribble) + int(dot) + int(drive) + int(dunk) + int(layup) + int(backdown) + int(postMove) + int(closeShot) + int(oBoard) + int(dBoard) + int(perDefense) + int(postDefense) + int(intimidation) + int(steal) + int(block) + int(reconition) + int(speed) + int(strength) + int(vertical)
#     ovr = num/24
#     return ovr

# def shooterF(three, mid, standShot, moveShot):
#     average = (int(three) + int(mid) + int(standShot) + int(moveShot)) / 4
#     return round(average)

# def playmakerF(passAcc, dribble, dot):
#     average = (int(passAcc) + int(dribble) + int(dot))/ 3
#     return round(average)

# def slashingF(drive, layup, dunk):
#     average = (int(drive) + int(layup) + int(dunk)) / 3
#     return round(average)

# def postF(backdown, postMove, closeShot, oBoard, dBoard):
#     average = (int(backdown) + int(postMove) + int(closeShot) + int(oBoard) + int(dBoard)) / 5
#     return round(average)

# def defenseF(perDefense, postDefense, intimidation, steal, block, reconition):
#     average = (int(perDefense) + int(postDefense) + int(intimidation) + int(steal) + int(block) + int(reconition)) / 6
#     return round(average)

# def physicalF(speed, strength, vertical):
#     average = (int(speed) + int(strength) + int(vertical)) / 3
#     return round(average)

# def ageFdig():
#     weights = [5, 3]
#     nums = [2, 3]

#     dig = random.choices(nums, weights=weights)
#     return dig

# def ageLdig(firstDigit):
#     nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#     if(firstDigit == 2):
#         weights = [1, 1, 2, 2, 3 , 3, 3, 3, 3, 3]
#     elif(firstDigit == 3):
#         weights = [5, 4, 3, 2, 1, 0.5, 0.5, 0.5, 0.5, 0.5]

#     dig = random.choices(nums, weights=weights)
#     return dig


# def getAge():
#     firstDigit = str(ageFdig())
#     lastDigit = str(ageLdig(int(firstDigit[1])))

#     ageString = firstDigit + lastDigit

#     age = firstDigit[1] + lastDigit[1]
#     return int(age)

# def getValue(ovr, age):
#     valOvr = ovr * 4
#     valAge = age * 2

#     val = valOvr - valAge
#     return val

# def birth():
#     fName = str(get_fname())
#     lName = str(get_lname())
  

#     pos = get_pos()

#     age = getAge()
#     height = str(get_height(pos))
#     weight = weight_func(height)
#     shooter = scale()
#     three = attribute(shooter)
#     mid = attribute(shooter)
#     standShot = attribute(shooter)
#     moveShot = attribute(shooter)

#     shooterA = shooterF(three, mid, standShot, moveShot)

#     playmaker = scale()
#     passAcc = attribute(playmaker)
#     dribble = attribute(playmaker)
#     dot = attribute(playmaker)

#     playmakerA = playmakerF(passAcc, dribble, dot)

#     slashing = scale()
#     drive = attribute(slashing)
#     dunk = attribute(slashing)
#     layup = attribute(slashing)

#     slashingA = slashingF(drive, dunk, layup)

#     post = scale()
#     backdown = attribute(post)
#     postMove = attribute(post)
#     closeShot = attribute(post)
#     oBoard = attribute(post)
#     dBoard = attribute(post)

#     postA = postF(backdown, postMove, closeShot, oBoard, dBoard)

#     defense = scale()
#     perDefense = attribute(defense)
#     postDefense = attribute(defense)
#     intimidation = attribute(defense)
#     steal = attribute(defense)
#     block = attribute(defense)
#     reconition = attribute(defense)

#     defenseA = defenseF(perDefense, postDefense, intimidation, steal, block, reconition)
    
#     physical = scale()
#     speed = attribute(physical)
#     strength = attribute(physical)
#     vertical = attribute(physical)

#     physicalA = physicalF(speed, strength, vertical)

    

#     ovr = getOverall(three, mid, standShot, moveShot, passAcc, dribble, dot, drive, dunk, layup, backdown, postMove, closeShot, oBoard, dBoard, perDefense, postDefense, intimidation, steal, block, reconition, speed, strength, vertical)
#     value = getValue(ovr, age)




#     player = Player(
#         first_name=fName,
#         last_name=lName,

#         pos=pos,

#         age = age,
#         height=height,
#         weight=weight,

#         ovr=ovr,
#         three=three,
#         mid=mid,
#         standShot=standShot,
#         moveShot=moveShot,

#         passAcc=passAcc,
#         dribble=dribble,
#         dot=dot,

#         drive=drive,
#         dunk=dunk,
#         layup=layup,
#         backdown=backdown,
#         postMove=postMove,
#         closeShot=closeShot,
#         oBoard=oBoard,
#         dBoard=dBoard,
        
#         perDefense=perDefense,
#         postDefense=postDefense,
#         intimidation=intimidation,
#         steal=steal,
#         block=block,
#         reconition=reconition,

#         speed=speed,
#         strength=strength,
#         vertical=vertical,

#         shooter = shooterA,
#         playmaker = playmakerA,
#         slashing = slashingA,
#         post = postA,
#         defense = defenseA,
#         physical = physicalA,
#         value = value


        


        





        
        
#     )
 
#     player.save()


#     # print("Player Statistics for", fName, lName)
#     # print("Position:", pos)
#     # print("Overall:", overall)
#     # print("Height:", height, "inches")
#     # print("Weight:", weight, "lbs")
#     # print("Three-Point Rating:", three)
#     # print("Mid-Range Rating:", mid)
#     # print("Close-Range Rating:", close)
#     # print("Dribble Rating:", dribble)
#     # print("Passing Rating:", passing)
#     # print("Perimeter Defense Rating:", perimeter_defense)
#     # print("Post Defense Rating:", post_defense)
#     # print("Steal Rating:", steal)
#     # print("Block Rating:", block)
# start = time.time()

# end = time.time()
# dur = end - start
# print(dur)
# # def test():
#     # cur = league.cursor()
#     # cur.execute("SELECT VERSION()")
#     # result = cur.fetchone()
#     # print("Database version:", result[0])
# # test()