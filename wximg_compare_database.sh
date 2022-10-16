#!/bin/bash

#---CONFIG---
WEBCAMURL='http://www.panorama-webcam.keepfree.de/upcam.jpg'
DATABASEPATH='database/'
DATABASEFILE='weathertags.csv'
#------------


datetime=$(date +%Y%m%d_%H%M)

echo 'Downloading file...'

wget $WEBCAMURL -O $DATABASEPATH$datetime.jpg -q

echo 'done.'
echo ' '

echo 'Image preview mode. Close preview window to continue.'
display $DATABASEPATH$datetime.jpg

echo ' '
echo 'Please select a cloud-cover option :'
echo '0 - clear/sunny'
echo '1 - only high/cirrus clouds'
echo '2 - few clouds'
echo '3 - partly cloudy'
echo '4 - cloudy'
echo '5 - fog'

read cloudcover

echo ' '
echo 'please select a percipitation option :'
echo '0 - no percipitation'
echo '1 - light rain'
echo '2 - heavy rain'
echo '3 - light snowfall'
echo '4 - heavy snowfall'
echo '5 - hail'

read percipitation

echo ' '
echo 'select a misc option'
echo '0 - none'
echo '1 - rainshowers in the distance'
echo '2 - snow on ground'
echo '3 - thunderstorm'

read misc

echo ' '
echo 'Weather-tags for this picture :'

case $cloudcover in
    0)
        echo '-> clear/sunny'
        ;;
    1)
        echo '-> only high/cirrus clouds'
        ;;
    2)
        echo '-> few clouds'
        ;;
    3)
        echo '-> partly cloudy'
        ;;
    4)
        echo '-> cloudy'
        ;;
    5)
        echo '-> fog'
        ;;
esac

case $percipitation in
    1)
        echo '-> light rain'
        ;;
    2)
        echo '-> heavy rain'
        ;;
    3)
        echo '-> light snowfall'
        ;;
    4)
        echo '-> heavy snowfall'
        ;;
    5)
        echo '-> hail'
        ;;
esac

case $misc in
    1)
        echo '-> rainshowers in the distance'
        ;;
    2)
        echo '-> snow on ground'
        ;;
    3)
        echo '-> thunderstorm'
        ;;
esac

echo ' '
echo 'Writing to database file...'

echo $datetime'.jpg,'$cloudcover','$percipitation','$misc | cat >> $DATABASEPATH$DATABASEFILE

echo 'done.'
