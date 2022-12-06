from datetime import datetime
import time

global dayX
dayX=1

def tokenYoutube():
    global DEVELOPER_KEY
    DEVELOPER_KEY = "<your developer key>"
    return DEVELOPER_KEY

def tokenTelegram():    
    global tokenTelegram
    tokenTelegram= '<your token telegram>'
    return tokenTelegram  

def channelid():
    global channelid
    # Enter your youtube channel id here
    channelid="UC-Ggv7TaOPWGKJLQw2y8Z9A"
    return channelid

def pubAfter():
    global publishedAfter
    timeCurrent=time.time() - 86400 * int(dayX) 
    dateStr =  datetime.fromtimestamp(timeCurrent)
    d1 = datetime.strptime(str(dateStr),"%Y-%m-%d %H:%M:%S.%f")
    publishedAfter= str(d1.strftime("%Y-%m-%dT%H:%M:%S.%fZ")) 
    print (publishedAfter)
    return publishedAfter  

def TestChannelTelegram():
    global testChannelTelegramId
    TestChannelTelegramId = '<id your telegram channel>'
    return TestChannelTelegramId 

def startTime():
    global startTimeNewVideo
    startTimeNewVideo = '13:43'
    return startTimeNewVideo  
if __name__ == "__configglobal__":
    pubAfter()    