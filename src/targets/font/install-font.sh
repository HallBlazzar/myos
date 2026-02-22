#!/bin/bash

wget https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/FiraCode.zip -O /tmp/FiraCode.zip
unzip /tmp/FiraCode.zip -d /tmp/firacode
mv /tmp/firacode /usr/share/fonts
rm /tmp/FiraCode.zip

mkfontscale /usr/share/fonts
mkfontdir /usr/share/fonts
fc-cache
