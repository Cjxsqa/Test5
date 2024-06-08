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
    'videoId': 'N9xcg0IOgws',
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


#os.system(f"ffmpeg -probesize 20200 -analyzeduration 15000 -re -i '{pr}' -vf \"transpose=1,transpose=1,transpose=1,transpose=1,setpts=0\" -tune zerolatency -threads 4 -map 0:p:6 -b:v 10000k -acodec copy -force_key_frames \"expr:gte(t,n_forced*2)\" -f flv rtmp://a.rtmp.youtube.com/live2/qtaa-xx6x-h99h-hjtp-1wf1")




os.system(f"ffmpeg -re -i '{pr}' -vf \"transpose=1,transpose=1,transpose=1,transpose=1,setpts=0\" -tune zerolatency -threads 4 -map 0:p:6 -b:v 10000k -acodec copy -f flv rtmp://a.rtmp.youtube.com/live2/qtaa-xx6x-h99h-hjtp-1wf1")