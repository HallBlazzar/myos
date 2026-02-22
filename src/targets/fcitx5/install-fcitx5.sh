#!/bin/sh

set -xe

flatpak install -y flathub org.fcitx.Fcitx5
flatpak install -y flathub org.fcitx.Fcitx5.Addon.McBopomofo

# Register to auto-start
mkdir -p /etc/skel/.config/autostart
cp /var/lib/flatpak/exports/share/applications/org.fcitx.Fcitx5.desktop /etc/skel/.config/autostart
