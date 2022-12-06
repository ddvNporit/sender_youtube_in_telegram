import json
from youtube.youtube_search_update import main as m
global response
global sendChat
def pJson():
    response=m()
    sendChat=''
    print(response)
    jsonData = json.dumps(response)
    dictData = json.loads(jsonData)
    if len(dictData["items"])>0:
        for items in dictData["items"]:
           # print("url:", "https://www.youtube.com/watch?v=" + items['id']['videoId'])
           url="https://www.youtube.com/watch?v=" + items['id']['videoId']
           sendChat =sendChat +url +"\n"
           print("Name:", items['snippet']['title'])
           print("Описание:", items['snippet']['description'])
    else:
        sendChat="Публикаций не обнаружено"
        print("Публикаций не обнаружено")
    return sendChat     
if __name__ == "__parsejson__":
       pJson()