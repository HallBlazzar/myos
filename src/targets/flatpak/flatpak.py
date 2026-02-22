from lbhelper import UpstreamPackages, HookScript
from pathlib import Path
from importlib.resources import files

core_flatpak_packages = UpstreamPackages(
    packages=[
        "flatpak",
        "gnome-software-plugin-flatpak",
    ],
    package_set_code="core-flatpak",
)

initialize_flatpak_hook = HookScript(
    get_script_file=lambda : Path(str(files(__package__) / "initialize-flatpak.sh")),
    hook_name="initialize-flatpak",
)

install_gnome_secrets_hook = HookScript(
    get_script_file=lambda : Path(str(files(__package__) / "install-gnome-secrets.sh")),
    hook_name="initialize-gnome-secrets",
)

targets = [
    core_flatpak_packages,
    initialize_flatpak_hook,
    install_gnome_secrets_hook,
]