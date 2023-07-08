
    
section = 'pre'

def advancePre():
    global section
    section = 'reg'
    
def advanceReg():
    global section
    section = 'playoff'
    
def advancePlayoff():
    global section
    section = 'draft'

def advanceDraft():
    global section
    section = 'free'
    
def advanceFree():
    global section
    section = 'pre'
    
num = int(input('gib num'))

if(num == 0):
    print(section)
if(num == 1):
    advancePre()
    print(section)
if(num == 2):
    advanceReg()
    print(section)