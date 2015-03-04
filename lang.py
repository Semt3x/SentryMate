import random

exitterms = ['bye', 'exit', 'cya', 'ciao']
waketerms = ['hey', 'oi']
acknoledgeterms = ['Rioukai', 'yup', 'On it', 'OK', 'Consider it done', 'my pleasure']
quickdb = ['echo', 'move']

def init():
    quickdb.extend(exitterms)
    quickdb.extend(waketerms)
    for w in waketerms:        
        actions.update({w.upper():shout})
    for e in exitterms:        
        actions.update({e.upper():nothing})
        
def process(msg):
    know = False
    for q in quickdb:
        if q.upper() in msg.upper():
            know = True
    if not know:
        return("I don't know that...")
    else:
        if " " in msg:
            return(actions[msg.split(' ',1)[0].upper()](msg.split(' ',1)[1]))
        else:
            return(actions[msg.upper()](""))
def saybye():
    return (random.choice(exitterms).title() + "!")    

def echo(msg):
    return(msg)
def shout(msg):
    return (random.choice(waketerms).title() + "!")
def nothing(msg):
    return("")

def move(msg):
    if msg == "":
        return("Tell me where")
    else:
        return(random.choice(acknoledgeterms).title() + "!")

actions = {'ECHO':echo, 'HEY':shout, 'OI':shout, 'MOVE':move}