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