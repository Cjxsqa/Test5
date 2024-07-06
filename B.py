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

pr = json.loads(response.text)["streamingData"]["hlsManifestUrl"]
print(pr)

from pathlib import Path
import json
import requests
session = requests.session()

#path = Path("cookies.json")
#Cookies = json.loads(path.read_bytes())
#Cookies = {'csrftoken': '1DuErYaNsJbg4uJN5YmM6iXDXDfU5BTs', 'rur': '"EAG\\0546049028904\\0541748757227:01f7405bc3fa8afb7689aa9c87ca5b498437097de75168fa1da6ee3edc93f15a1107e3f0"', 'mid': 'Zlq3ZgALAAE3E4MskrxsJfcU7-yi', 'ds_user_id': '6049028904', 'ig_did': '14168AAB-5780-41FA-80F0-BA4F22686941', 'sessionid': '6049028904%3AxATX5Nq7jp4tI1%3A10%3AAYcy5I6b1RnJ9Vwj9VL3QiKYgt8NrYxOcEaVGPPd7A'}
Cookies = {'csrftoken': 'jV2ZJv6zdmIOA2pXGl5dv9Upmd57gVe5', 'rur': '"CCO\\05451941737982\\0541751821562:01f785ef80e85d2767ffef3b27a89dd287eb5709861d683e408bbe998c82835d9ba3d6a8"', 'mid': 'Zol5dwALAAHjbg41JoUG6CYX74K0', 'ds_user_id': '51941737982', 'ig_did': 'D3ADD960-C5E1-4054-9147-BBA1D67EF6DB', 'sessionid': '51941737982%3ANXXMl0BAgoeTyZ%3A16%3AAYfSwsnStPaWjs3euzZNx3ZMh--livddKpbI8g95Fw'}

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
    'broadcast_message': 'Test5',
    'internal_only': 'false',
    'preview_height': '720',
    'preview_width': '1080',
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




os.system(f"ffmpeg -re -i '{pr}' -vf transpose=1 -threads 4 -map 0:p:6 -vcodec libx264 -b:v 9000k -acodec copy -preset ultrafast -f flv '{upload_url}'")
