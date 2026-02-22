from pathlib import Path
from importlib.resources import files

from lbhelper import HookScript


install_netbird_hook = HookScript(
    get_script_file=lambda : Path(str(files(__package__) / "install-netbird.sh")),
    hook_name="install-netbird",
)

targets = [
    install_netbird_hook,
]