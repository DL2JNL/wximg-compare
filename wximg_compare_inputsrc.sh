#!/bin/bash

# WXimg-compare inputfile source script
#
# Add corntab :
# For every minute :
# * * * * * /path/to/wximg_compare/wximg/compare_inputsrc.sh
# or for every 10 minutes
# */10 * * * * /path/to/wximg_compare/wximg/compare_inputsrc.sh
# or for every hour
# 0 * * * * /path/to/wximg_compare/wximg/compare_inputsrc.sh

#---CONFIG---
# input options : local file, file from website, video device
FILEPATH='/home/jan/Pictures/Blockhaus/latest.jpg'
WEBURL='https://example.com/example.jpg'
VIDEOSOURCE='/dev/video0'
# path to WXimg-compare inputfile
INPUTFILE='/home/jan/wximg_compare/input/input.jpg'
# time to wait before copy/download (e.g. if sourcefile is updated every minute at 0 seconds)
SLEEPTIME=10
#------------

sleep 10

# uncomment for local file
cp -f $FILEPATH $INPUTFILE

# uncomment for file from website
#wget $WEBCAMURL -O $INPUTFILE

# uncomment for video device
#fswebcam --resolution 1920x1080 --jpeg 85 --device $VIDEOSOURCE $INPUTFILE
