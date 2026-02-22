from pathlib import Path
from importlib.resources import files

from lbhelper import HookScript


install_vagrant_hook = HookScript(
    get_script_file=lambda : Path(str(files(__package__) / "install-vagrant.sh")),
    hook_name="install-vagrant",
)

targets = [
    install_vagrant_hook,
]