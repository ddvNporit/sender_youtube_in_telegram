# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python
import os
import googleapiclient.discovery
## глобальные переменные
from configglobal import tokenYoutube as ty
from configglobal import channelid as chId
from configglobal import pubAfter as pA
global response
#class YoutubeSearch:
def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = ty()

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.search().list(
        part="snippet",
        channelId=chId(),
        publishedAfter=pA()
    )
    response = request.execute()
    return response
    
if __name__ == "__youtube_search_update__":
       
       main()