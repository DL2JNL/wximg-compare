#!/bin/bash

sleep 30

datetime=$(date +%d.%m.%Y_%H:%M)
weather=$(python3 /home/jan/wximg_compare/wximg_compare.py)

echo $datetime | cat >> '/home/jan/wximg_compare/log.txt'
echo $weather | cat >> '/home/jan/wximg_compare/log.txt'
echo '----------' | cat >> '/home/jan/wximg_compare/log.txt'

