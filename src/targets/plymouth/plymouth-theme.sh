#!/bin/sh

set -xe

if [ -e /usr/sbin/plymouth-set-default-theme ] && [ -e /usr/share/plymouth/themes/homeworld ]
then
    # https://wiki.debian.org/DebianArt/Themes
    plymouth-set-default-theme homeworld
fi