import requests
import os
from pathlib import Path
from importlib.resources import files

from lbhelper import HookScript, render_template_to_file, StaticFile

# Based on https://github.com/nagygergo/jetbrains-toolbox-install/blob/master/jetbrains-toolbox.sh
# As jetbrains toolbox cannot be installed system-wised, alternatively, install it in /etc/skel.

def get_toolbox_latest_release_download_url(url: str) -> str:
    response = requests.get(url).json()
    return response["TBA"][0]["downloads"]["linux"]["link"]

toolbox_release_api = "https://data.services.jetbrains.com/products/releases?code=TBA&latest=true&type=release"

toolbox_tarball_download_url = get_toolbox_latest_release_download_url(toolbox_release_api)
toolbox_tarball_filename = os.path.basename(toolbox_tarball_download_url)
toolbox_tarball_save_path = Path("/tmp/toolbox_tarball_filename")

toolbox_install_dir_path = Path("/etc/skel/.local/share/JetBrains/Toolbox")
# relative to toolbox_symlink_dir_path
toolbox_executable_relative_path = "../share/JetBrains/Toolbox/bin/jetbrains-toolbox"
toolbox_symlink_dir_path = Path("/etc/skel/.local/bin")
toolbox_icon_path = Path("/opt/jetbrains-toolbox/toolbox.svg")

autostart_dir_path = Path("/etc/skel/.config/autostart")

install_toolbox_hook = HookScript(
    get_script_file=lambda : render_template_to_file(
        Path(str(files(__package__) / "install-toolbox.sh.j2")),
        toolbox_tarball_save_path=toolbox_tarball_save_path,
        toolbox_tarball_download_url=toolbox_tarball_download_url,
        toolbox_install_dir_path=toolbox_install_dir_path,
        toolbox_symlink_dir_path=toolbox_symlink_dir_path,
        toolbox_executable_relative_path=toolbox_executable_relative_path,
        autostart_dir_path=autostart_dir_path,
    ),
    hook_name="install-toolbox",
)

# register to desktop app search path
toolbox_entry_file = StaticFile(
    get_source_file=lambda: render_template_to_file(
        Path(str(files(__package__) / "jetbrains-toolbox.desktop.j2")),
        toolbox_icon_path=toolbox_icon_path,
    ),
    target_filepath=Path("/etc/skel/.local/share/applications/jetbrains-toolbox.desktop"),
)

toolbox_icon_file = StaticFile(
    get_source_file=lambda: Path(str(files(__package__) / "toolbox.svg")),
    target_filepath=toolbox_icon_path,
)

targets = [
    install_toolbox_hook,
    toolbox_entry_file,
    toolbox_icon_file,
]
