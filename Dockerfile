FROM ubuntu:22.04
RUN \
    --mount=type=cache,target=/var/cache/apt \
    apt-get -y update && add-apt-repository ppa:savoury1/ffmpeg4 && DEBIAN_FRONTEND=noninteractive apt-get -y install tzdata apt-utils && apt-get -y install sudo ffmpeg python3 python3-pip && pip3 install requests
ADD main.py .
ADD cookies.json .
