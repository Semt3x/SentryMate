import random

members = {}
coreLevel = 5


def initCore(level):
    if(level == 0):
        return "nop"
        #init core with max functions
    elif(level == 1):
        return "nop"
        #init core with less functions
    elif(level == 5):
        return "yup"
        #init core in simulation mode

def getPicture():
    #do stuff with camera then get a Picture as png
    return True

def getVideoStream():
    #do stuff then return video stream
    return True

def getOrder():
    if(coreLevel == 5):
        return bool(random.getrandbits(1))
    else:
        #dostuff
        return True
    
def tweetThat(msg):
    #do stuff with msg and Twitter API
    return True
