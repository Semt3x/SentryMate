import random
import core

exitterms = ['bye', 'exit', 'cya', 'ciao']
waketerms = ['hey', 'oi']
acknoledgeterms = ['Rioukai', 'yup', 'On it', 'OK', 'Consider it done', 'my pleasure']
negativeterms = ['no', 'nope', 'negative', 'niet', 'Iie']
quickdb = ['echo', 'move', 'help', 'tweet']
    
def init():
    core.initCore(5)
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
        try:
            if " " in msg:
                return(actions[msg.split(' ',1)[0].upper()](msg.split(' ',1)[1]))
            else:
                return(actions[msg.upper()](""))
        except:
            return("You typed it wrong !")
                
def saybye():
    return (random.choice(exitterms).title() + "!")

def echo(msg):
    if(msg == ""):
        return("Tell me what to say !")
    return(msg.upper())
def shout(msg):
    return (random.choice(waketerms).title() + "!")
def nothing(msg):
    return("")

def help(msg):
    msg = "I do know :"
    for q in quickdb:
        msg = msg + "\n - "+q
    return(msg)

def move(msg):
    if msg == "":
        return("Tell me where")
    else:
        if(core.getOrder()):
            return(random.choice(acknoledgeterms).title() + "!")
        else:
            return(random.choice(negativeterms).title() + "!")

def getInfo(msg):
    memb = msg.split(" ")
    memb.pop(0)
    smemb = ""
    for m in memb:
        smemb = m + " "
    core.getInfo(smemb)
    
def tweet(msg):
    if msg != "":
        if (core.tweetThat(msg)):
            return(random.choice(acknoledgeterms).title() + "!")
        else:
            return(random.choice(negativeterms).title() + "!")
        

actions = {'ECHO':echo, 'HEY':shout, 'OI':shout, 'MOVE':move, 'HELP':help, 'TWEET':tweet}