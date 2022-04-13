#!/bin/sh

wget https://raw.githubusercontent.com/everest-linux/xfetch/main/xfetch.py
cp xfetch.py xfetch
chmod +x xfetch
mv xfetch /usr/bin
