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
    'videoId': 'E3swaksCIaw',
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

#pr = response.json()['streamingData']["adaptiveFormats"]
#l = []
#for __ in pr:
#    if "1080p" in str(__) and "mp4" in str(__):
#        l.append(__)
#    if "AUDIO_QUALITY_MEDIUM" in str(__) and not 'isDrc' in str(__):
#        l.append(__)
#video = l[0]['url']
#audio = l[-1]['url']
#print(video)
#print(audio)



#os.system(f"ffmpeg -re -i '{pr}' -vf \"transpose=1,transpose=1,transpose=1,transpose=1,drawtext=fontfile=_.ttf:text='FunnyBunny - YT':fontcolor=white:fontsize=68:box=1:boxcolor=black@0.5:boxborderw=5:x=w-tw:y=h-th\" -map 0:v:4 -map 0:a -threads 4 -crf 0 -b:v 10000k -c:a aac -g 30 -b:a 384k -f tee \"[select=v:4,a:1] rtmp://a.rtmp.youtube.com/live2/j32f-zj48-1axx-m9g1-1zms [select=v:4,a:1] rtmp://a.rtmp.youtube.com/live2/zvmf-1yjp-jzek-01pw-b4js\"")


#os.system(f"ffmpeg -re -i '{video}' -i '{audio}' -vf \"transpose=1,transpose=1,transpose=1,transpose=1,drawtext=fontfile=_.ttf:text='FunnyBunny - YT':fontcolor=white:fontsize=68:box=1:boxcolor=black@0.5:boxborderw=5:x=w-tw:y=h-th\" -threads 4 -crf 0 -b:v 10000k -c:a aac -g 30 -b:a 384k -f flv rtmp://a.rtmp.youtube.com/live2/zvmf-1yjp-jzek-01pw-b4js -vcodec copy -acodec copy -f flv ")


#os.system(f"ffmpeg -rtbufsize 256M -re -i '{pr}' -vf \"transpose=1,drawtext=fontfile=_.ttf:text='FunnyBunny - YT':fontcolor=white:fontsize=68:box=1:boxcolor=black@0.5:boxborderw=5:x=w-tw:y=h-th\" -threads 4 -map 0:p:5 -crf 0 -b:v 10000k -c:a aac -g 30 -b:a 384k -f flv \"rtmps://edgetee-upload-maa2-1.xx.fbcdn.net:443/rtmp/17936757614744903?s_bl=1&s_fbp=tir3-1&s_prp=maa2-1&s_spl=1&s_sw=0&s_tids=1&s_vt=ig&a=AbyZGAvU6xCVbZ-U\"")


#os.system(f"ffmpeg -re -i '{pr}' -vf transpose=1 -map 0:p:5 -pix_fmt yuv420p -threads 4 -vb 400k -deinterlace -c:v libx264 -c:a aac -g 30 -b:a 384k -f flv \"rtmp://edgetee-upload-maa2-1.xx.fbcdn.net:443/rtmp/17936757614744903?s_bl=1&s_fbp=tir3-1&s_prp=maa2-1&s_spl=1&s_sw=0&s_tids=1&s_vt=ig&a=AbyZGAvU6xCVbZ-U\"")







from pathlib import Path
import json
import requests
session = requests.session()

#path = Path("cookies.json")
#Cookies = json.loads(path.read_bytes())
Cookies = {'csrftoken': '1DuErYaNsJbg4uJN5YmM6iXDXDfU5BTs', 'rur': '"EAG\\0546049028904\\0541748757227:01f7405bc3fa8afb7689aa9c87ca5b498437097de75168fa1da6ee3edc93f15a1107e3f0"', 'mid': 'Zlq3ZgALAAE3E4MskrxsJfcU7-yi', 'ds_user_id': '6049028904', 'ig_did': '14168AAB-5780-41FA-80F0-BA4F22686941', 'sessionid': '6049028904%3AxATX5Nq7jp4tI1%3A10%3AAYcy5I6b1RnJ9Vwj9VL3QiKYgt8NrYxOcEaVGPPd7A'}
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

params = {
    'target_user_id': f'{id}',
    'hl': 'en',
}
#print(session.headers)
#session.cookies.update({"wd": "1280x720", "locale": "en_US", })
#print(session.cookies)
#response = session.get('https://www.instagram.com/api/v1/live/web_info/', params=params)
#print(response.text)
data = {
    'broadcast_message': 'Test5',
    'internal_only': 'false',
    'preview_height': '854',
    'preview_width': '480',
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


#rr = session.post(f"https://www.instagram.com/api/v1/live/18051720028639043/end_broadcast/")
print(rr.text)
#print(rr.text)












#t5 = session.post("https://www.instagram.com/api/v1/live/18024036962482997/end_broadcast/")
#print(t5.text)



#os.system(f"ffmpeg -re -i '{video}' -i '{audio}' -vf transpose=1 -c:v libx264 -g 30 -c:a aac -f flv '{upload_url}'")

#rt = requests.get(pr)








RES= re.findall("\d{2,}x([0-9]+)", requests.get(pr).text).index('480')

print("RESOLTUOOMG : ", RES)
prin = int(RES)
print(pr)

#os.system(f"ffmpeg -re -i '{pr}' -vf transpose=1 -acodec copy -f fifo -fifo_format flv -drop_pkts_on_overflow 1 -attempt_recovery 1 -recovery_wait_time 1 -map 0:v:6 -map 0:a:1 '{upload_url}'")


#os.system(f"ffmpeg -user_agent \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36\" -http_persistent 0 -rtbufsize 256M -re -i '{pr}' -max_muxing_queue_size 9999 -vf \"transpose=1,transpose=1,transpose=1,transpose=1\" -threads 4 -map 0:p:{prin} -crf 0 -b:v 10000k -c:a aac -g 30 -b:a 384k -f flv 'rtmp://a.rtmp.youtube.com/live2/qtaa-xx6x-h99h-hjtp-1wf1' -vcodec copy -acodec copy -f flv '{upload_url}'")




os.system(f"ffmpeg -user_agent \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36\" -http_persistent 0 -rtbufsize 256M -re -i '{pr}' -max_muxing_queue_size 9999 -vf \"transpose=1\" -threads 8 -map 0:p:{prin} -c:v libx264 -b:v 10000k -acodec copy -f flv '{upload_url}'")