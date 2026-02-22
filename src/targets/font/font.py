from lbhelper import HookScript
from importlib.resources import files
from pathlib import Path

# See https://gist.github.com/matthewhartman/7b1661dbe6ff26a231e4
install_fonts_hook = HookScript(
    get_script_file=lambda : Path(str(files(__package__) / "install-font.sh")),
    hook_name="install-fonts",
)

targets = [
    install_fonts_hook
]