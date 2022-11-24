#!/bin/bash

#---CONFIG---
INPUTFILE='/home/jan/wximg_compare/input/input.jpg'
DATABASEPATH='/home/jan/wximg_compare/database/'
DATABASEFILE='weathertags.csv'
#------------

datetime=$(date +%Y%m%d_%H%M)

echo 'Copying file...'

cp -f $INPUTFILE $DATABASEPATH$datetime.jpg

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
echo '1 - rain'
echo '2 - snowfall'
echo '3 - hail'

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
        echo '-> rain'
        ;;
    2)
        echo '-> snowfall'
        ;;
    3)
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
