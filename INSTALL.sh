#!/bin/sh

echo "[ i ] Getting executable..."
wget https://raw.githubusercontent.com/everest-linux/xfetch/main/xfetch.py
echo "[ i ] Installing executable..."
cp xfetch.py xfetch
chmod +x xfetch
mv xfetch /usr/bin
echo "[ i ] xfetch installed successfully."
