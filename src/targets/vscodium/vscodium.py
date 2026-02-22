from pathlib import Path
from importlib.resources import files

from lbhelper import HookScript


install_vscodium_hook = HookScript(
    get_script_file=lambda : Path(str(files(__package__) / "install-vscodium.sh")),
    hook_name="install-vscodium",
)

targets = [
    install_vscodium_hook,
]