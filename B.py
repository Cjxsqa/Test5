import requests
import re
import json
import os

cookies = {
    'PREF': 'hl=en&tz=UTC',
    'SOCS': 'CAI',
    'GPS': '1',
    'YSC': 'ypCO9qGoKSY',
    'VISITOR_INFO1_LIVE': 'qBJvehrqV6s',
    'VISITOR_PRIVACY_METADATA': 'CgJJThIEGgAgKA%3D%3D',
}

headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'com.google.ios.youtube/19.09.3 (iPhone14,3; U; CPU iOS 15_6 like Mac OS X)',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-us,en;q=0.5',
    'Sec-Fetch-Mode': 'navigate',
    'X-Youtube-Client-Name': '5',
    'X-Youtube-Client-Version': '19.09.3',
    'Origin': 'https://www.youtube.com',
}

params = {
    'key': 'AIzaSyB-63vPrdThhKuerbB2N_l7Kwwcxj6yUAc',
    'prettyPrint': 'false',
}

json_data = {
    'context': {
        'client': {
            'clientName': 'IOS',
            'clientVersion': '19.09.3',
            'deviceModel': 'iPhone14,3',
            'userAgent': 'com.google.ios.youtube/19.09.3 (iPhone14,3; U; CPU iOS 15_6 like Mac OS X)',
            'hl': 'en',
            'timeZone': 'UTC',
            'utcOffsetMinutes': 0,
        },
    },
    'videoId': 'Bo6NF3-cq_I',
    'playbackContext': {
        'contentPlaybackContext': {
            'html5Preference': 'HTML5_PREF_WANTS',
        },
    },
    'contentCheckOk': True,
    'racyCheckOk': True,
}
response = requests.post(
    'https://www.youtube.com/youtubei/v1/player',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)

#pr = json.loads(response.text)["streamingData"]["hlsManifestUrl"]
#print(pr)

from pathlib import Path
import json
import requests
session = requests.session()

#path = Path("cookies.json")
#Cookies = json.loads(path.read_bytes())
#Cookies = {'csrftoken': '1DuErYaNsJbg4uJN5YmM6iXDXDfU5BTs', 'rur': '"EAG\\0546049028904\\0541748757227:01f7405bc3fa8afb7689aa9c87ca5b498437097de75168fa1da6ee3edc93f15a1107e3f0"', 'mid': 'Zlq3ZgALAAE3E4MskrxsJfcU7-yi', 'ds_user_id': '6049028904', 'ig_did': '14168AAB-5780-41FA-80F0-BA4F22686941', 'sessionid': '6049028904%3AxATX5Nq7jp4tI1%3A10%3AAYcy5I6b1RnJ9Vwj9VL3QiKYgt8NrYxOcEaVGPPd7A'}
Cookies = {"csrftoken": "nStbIsIYUO0X295MwaOVbjFAaqso2g9p", "rur": "\"CCO\\0548510847248\\0541751905491:01f7eae16c1314ba80ecbef1455f19ddbfc1f89a4c275e27db21a79eea89ad661d92e577\"", "mid": "Zki-HwALAAHGxyPe3ATMxcewqF5-", "ds_user_id": "8510847248", "ig_did": "174B4DF3-F44A-43B1-8FE5-B65885FB0256", "sessionid": "8510847248%3A13LbljrII1IAmd%3A18%3AAYdyWz2pCoG0uD7qyQLWzCZ2qhp3Cm_XJBGMQ2sEbw"}

#{'csrftoken': 'jV2ZJv6zdmIOA2pXGl5dv9Upmd57gVe5', 'rur': '"CCO\\05451941737982\\0541751821562:01f785ef80e85d2767ffef3b27a89dd287eb5709861d683e408bbe998c82835d9ba3d6a8"', 'mid': 'Zol5dwALAAHjbg41JoUG6CYX74K0', 'ds_user_id': '51941737982', 'ig_did': 'D3ADD960-C5E1-4054-9147-BBA1D67EF6DB', 'sessionid': '51941737982%3ANXXMl0BAgoeTyZ%3A16%3AAYfSwsnStPaWjs3euzZNx3ZMh--livddKpbI8g95Fw'}

#{'csrftoken': 'hD60PUDcPudwdXJfCrLDizAhwvFnM6fy', 'rur': '"LDC\\05451941737982\\0541749362678:01f7bec08838ecd8377b00be80c84aa81f940ec9702f26bf7dea236f64c4f5d207eae087"', 'mid': 'ZmP0cwALAAEaLxU78y0py1K_CUDL', 'ds_user_id': '51941737982', 'ig_did': 'C01E64D7-0957-4F3E-B597-66EA7FD754E1', 'sessionid': '51941737982%3AuuSYrABkxAAqLf%3A21%3AAYf4eoCJOvh8BfDgBCvABtlWv3K5b31ctAzdMKSmrw'}

csrf = Cookies["csrftoken"]
id = Cookies["ds_user_id"]

#print(cookies)  # save them to file as JSON
cookies = requests.utils.cookiejar_from_dict(Cookies)
#print(cookies)
session.cookies.update(cookies)
#print(session.headers) # load cookiejar to current session
#print(session.get("https://www.instagram.com/settings/help/account_status/?hl=en").text)  # te
#import requests


headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'Priority': 'u=1, i',
    'Referer': 'https://www.instagram.com/settings/help/account_status/?hl=en',
    'sec-ch-prefers-color-scheme': 'light',
#    'sec-ch-ua': '"Chromium";v="125", "Not.A/Brand";v="24"',
#    'sec-ch-ua-full-version-list': '"Chromium";v="125.0.6422.60", "Not.A/Brand";v="24.0.0.0"',
#    'sec-ch-ua-mobile': '?0',
#    'sec-ch-ua-model': '""',
#    'sec-ch-ua-platform': '"Linux"',
#    'sec-ch-ua-platform-version': '"4.19.191"',
#    'sec-fetch-dest': 'empty',
#    'sec-fetch-mode': 'cors',
#    'sec-fetch-site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
#    'x-asbd-id': '129477',
    'x-csrftoken': f'{csrf}',
    'x-ig-app-id': '936619743392459',
#    'x-ig-app-id': '743845927482847',
 #   'x-ig-www-claim': 'hmac.AR1_ueWdmxzSLaL-obCxlwYWH_OHumpsDQC2featPzTqv7Ay',
    'X-Requested-With': 'XMLHttpRequest',
}


session.headers = headers
#print(session.headers)
#session.headers.update({"x-csrftoken": f"{csrf}"})

#params = {
#    'target_user_id': f'{id}',
#    'hl': 'en',
#}
#print(session.headers)
#session.cookies.update({"wd": "1280x720", "locale": "en_US", })
#print(session.cookies)
#response = session.get('https://www.instagram.com/api/v1/live/web_info/', params=params)
#print(response.text)
data = {
    'broadcast_message': 'Adventure night - Batman Arkham knights 🦇',
    'internal_only': 'false',
#    'preview_height': '1080',
#    'preview_width': '1920',
    'source_type': '5',
    'broadcast_type': 'RTMP',
    'visibility': '0',
#    'disable_speed_test': '1',
#    'is_premium': '1'
}


res = session.post("https://www.instagram.com/api/v1/live/create/", params={'hl': 'en'}, data=data)
p6 = res.json()
print(p6)
broadcastid = p6['broadcast_id']
upload_url = p6['upload_url']
print(upload_url)
print(broadcastid)





#dat ={'should_send_notifications': 1}

rr = session.post(f"https://www.instagram.com/api/v1/live/{broadcastid}/start/", data={'should_send_notifications': 1})



#os.system(f"ffmpeg -probesize 200 -analyzeduration 100 -re -i '{pr}' -vf \"transpose=1,transpose=1,transpose=1,transpose=1,setpts=0\" -tune zerolatency -threads 4 -map 0:p:6 -b:v 8000k -acodec copy -g 60 -f flv rtmp://a.rtmp.youtube.com/live2/qtaa-xx6x-h99h-hjtp-1wf1")

#hhhh = "https://fa723fc1b171.us-west-2.playback.live-video.net/api/video/v1/us-west-2.196233775518.channel.uJXcF39rPp9m.m3u8?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzM4NCJ9.eyJhd3M6Y2hhbm5lbC1hcm4iOiJhcm46YXdzOml2czp1cy13ZXN0LTI6MTk2MjMzNzc1NTE4OmNoYW5uZWwvdUpYY0YzOXJQcDltIiwiYXdzOmFjY2Vzcy1jb250cm9sLWFsbG93LW9yaWdpbiI6Imh0dHBzOi8va2ljay5jb20saHR0cHM6Ly9wbGF5ZXIua2ljay5jb20saHR0cHM6Ly9hZG1pbi5raWNrLmNvbSxodHRwczovL3d3dy5nc3RhdGljLmNvbSxodHRwczovLyoua2ljay5saXZlLGh0dHBzOi8vYmV0YS5raWNrLmNvbSIsImF3czpzdHJpY3Qtb3JpZ2luLWVuZm9yY2VtZW50IjpmYWxzZSwiZXhwIjoxNzIwMzI2Mzk0fQ.kIiZGzDOy2shuDSQSVfHHOGP29ZKFyAvDlB5uD64MwUUyk5k4kL_-9eJqWfYEHjxhQtYhTjQmQOw981ghrWTUBLzaNuKMBqXkUaCFrgB5K46fnIGuq1oO2AI_qnrzjqU"


headers = {
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-platform': '"Android"',
    'dnt': '1',
    'sec-ch-ua-mobile': '?1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'origin': 'https://dlive.tv',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://dlive.tv/',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'priority': 'u=1, i',
}

json_data = {
    'playlisturi': 'https://livestreamb.prdv3.dlivecdn.com/funnybunny-yt/1720543344/src/live.m3u8'
}

esponse44 = requests.post('https://live.prd.dlive.tv/hls/sign/url', headers=headers, json=json_data).text
print(esponse44)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"playlisturi":"https://livestreamc.prdv3.dlivecdn.com/unitynews/1718128583/src/live.m3u8"}'
#response = requests.post('https://live.prd.dlive.tv/hls/sign/url', headers=headers, data=data)


#os.system("ffmpeg -headers $'User-Agent: Mozilla/5.0 (Android; vivo V2311) Android/14 version/1.17.74\r\nHost: livestreamc.prdv3.dlivecdn.com\r\nConnection: Keep-Alive\r\nAccept-Encoding: identity\r\nReferer: https://dlive.tv/\r\n' -re -i 'https://livestreamc.prdv3.dlivecdn.com/dlive-knfgmgrycm/1718467298/720p/live.m3u8' -vf transpose=1 -c:a copy -preset ultrafast -tune zerolatency -f mpegts -muxrate 7599900 udp://127.0.0.1:47333 | ffmpeg -f mpegts -i udp://127.0.0.1:47333 -vcodec libx264 -acodec copy -preset ultrafast -tune zerolatency -f flv '{upload_url}'")




os.system(f"ffmpeg -headers $'User-Agent: Mozilla/5.0 (Android; vivo V2311) Android/14 version/1.17.74\r\nHost: livestreamc.prdv3.dlivecdn.com\r\nConnection: Keep-Alive\r\nAccept-Encoding: identity\r\nReferer: https://dlive.tv/\r\n' -re -i '{esponse44}' -vf transpose=1 -threads 4 -vcodec libx264 -b:v 9000k -acodec copy -preset ultrafast -f flv '{upload_url}'")
