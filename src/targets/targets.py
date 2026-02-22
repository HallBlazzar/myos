from .flatpak import targets as flatpak
from .fcitx5 import targets as fcitx5
from .jetbrains_toolbox import targets as jetbrains_toolbox
from .liveboot_config import targets as liveboot_config
from .netbird import targets as netbird
from .nextcloud import targets as nextcloud
from .obsidian import targets as obsidian
from .plymouth import targets as plymouth
from .shell import targets as shell
from .vscodium import targets as vscodium
from .device import targets as device
from .discord import targets as discord
from .gnome import targets as gnome
from .system_core import targets as system_core
from .tools import targets as tools
from .live_installer import targets as live_installer
from .zerotier import targets as zerotier
from .font import targets as font
from .grub import targets as grub
from .firefox_esr import targets as firefox_esr
from .vagrant import targets as vagrant

targets = [
    # liveboot related boot settings
    liveboot_config,

    device,
    system_core,

    # system booting load screen
    plymouth,

    # gnome environment
    gnome,
    font,

    # live-installer
    live_installer,

    # core tools
    tools,

    # flatpak packages
    flatpak,
    # relies on flatpak
    fcitx5,

    # other 3rd-party dev tools
    jetbrains_toolbox,
    netbird,
    nextcloud,
    obsidian,
    vscodium,
    discord,
    zerotier,
    vagrant,

    # firefox esr config
    firefox_esr,

    # prettify shell
    shell,

    # grub theme patch
    grub,
]
