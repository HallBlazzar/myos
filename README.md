# MyOS

MyOS is a customized Debian image based on the [lbhelper](https://hallblazzar.github.io/lbhelper/source/index.html).
It's not only a demo project of the `lbhelper` but a system I use in my daily basis(on [Dell Pro 14 Laptop](https://www.dell.com/en-ie/shop/laptop-computers-2-in-1-pcs/dell-pro-14-laptop/spd/dell-pro-pc14255-laptop/gcto_pc14255_emea?redirectTo=SOC))

## What does the image contain?

1. [Calamares](https://calamares.io/) based system installer(for live system).
2. [Poly-Dark](https://github.com/shvchk/poly-dark) Grub(for installed system).
3. GNOME desktop environment.
4. fcitx5 input with configuration tool and [McBopomofo](https://github.com/openvanilla/McBopomofo). The system will be pre-configured with fcitix5 and input methods enabled.
5. Firefox ESR with vertical tabs, [Workona](https://workona.com/) and [Undo Tabs Button](https://addons.mozilla.org/en-US/firefox/addon/undo-closed-tabs-revived/).
6. Flatpack with pre-configured [FlatHub](https://flathub.org/en) source.
7. [GNOME Secrets](https://apps.gnome.org/Secrets/) (from FlatHub)
8. Pre-configured and pre-enabled GNOME extensions
    - [Lock Key](https://extensions.gnome.org/extension/36/lock-keys/)
    - [Vitals](https://extensions.gnome.org/extension/1460/vitals/)
    - [Hibernate](https://extensions.gnome.org/extension/755/hibernate-status-button/)
    - [Move Clock](https://extensions.gnome.org/extension/2/move-clock/)
    - [Dash to Dock](https://extensions.gnome.org/extension/307/dash-to-dock/)
    - [No Overview](https://extensions.gnome.org/extension/4099/no-overview/)
9. [Jetbrains ToolBox](https://www.jetbrains.com/help/toolbox-app/toolbox-app-silent-installation.html)
10. [NetBird VPN Client](https://docs.netbird.io/get-started/install/linux).
11. [Obsidian App Image](https://help.obsidian.md/install).
12. Plymouth with [homeworld theme](https://wiki.debian.org/DebianArt/Themes).
13. Pre-configured ZSH (with [OhMyZsh](https://ohmyz.sh/) and [Starship](https://starship.rs/). Also with extension:
    - [Auto Suggestions](https://github.com/zsh-users/zsh-autosuggestions)
    - [Syntax Highlight](https://github.com/zsh-users/zsh-syntax-highlighting.git)
14. [Vagrant](https://developer.hashicorp.com/vagrant) and [libvirt extension](https://vagrant-libvirt.github.io/vagrant-libvirt/).
15. [VSCodium](https://vscodium.com/).
16. [ZeroTier VPN Client](https://www.zerotier.com/).
17. Dell Pro 14 related drivers.
18. [Discord deb](https://discord.com/download).
19. Git.
20. [YQ](https://github.com/mikefarah/yq).
21. [JQ](https://jqlang.org/).
22. OpenSSH client and server.
23. [PCManFM](https://pcmanfm.com/) file manager.
24. [WireShark](https://www.wireshark.org/).
25. Gedit.
26. Vim.
27. [Ptyxis Termina](https://gitlab.gnome.org/chergert/ptyxis).
28. [Alacarte](https://gitlab.gnome.org/GNOME/alacarte) menu editor.
29. [Network Manager Connection Editor](https://packages.debian.org/unstable/nm-connection-editor).
30. CURL.
31. [QEMU](https://www.qemu.org/) and [virt-manager](https://virt-manager.org/).
32. [distrobox](https://distrobox.it/).
33. [Android Studio related dependencies](https://developer.android.com/studio/install#64bit-libs).

## How To Build

### Requirements

1. Debian based system. Other Linux distros might work but requires additional setup. See [live-build official doc](https://live-team.pages.debian.net/live-manual/html/live-manual/installation.en.html)
2. At least 64 GB free disk spaces.
3. Live Build
   ```
   sudo apt install -y live-build
   ```
4. UV
   ```
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
   Note that `uv` is a per-user basis tool. The build process requires root permission, which means you also need to install it for root user.

### Build Instructions

1. Clone project and enter project root
   ```
   git clone https://github.com/HallBlazzar/myos
   cd myos
   ```
2. Install required packages
   ```
   uv sync
   ```
3. Build image
   ```
   cd src
   sudo uv run main.py
   ```
   
The build process will take 1-2 hours depends on hardware and network bandwidth. Once image built, you can find artifacts in the `src/build`. The live system ISO is `myos-amd64.hybrid.iso`, which you can boot it as VM(to validate/test it before deploying) or create a bootable device via tools like [ISO Image Writer](https://community.kde.org/ISOImageWriter) or [Rufus](https://rufus.ie/en/).
