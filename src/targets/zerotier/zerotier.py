from lbhelper import HookScript

from importlib.resources import files
from pathlib import Path

# see https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/desktop_migration_and_administration_guide/extensions-enable
install_zerotier_hook = HookScript(
    get_script_file=lambda : Path(str(files(__package__) / "install-zerotier.sh")),
    hook_name="install-zerotier",
)

targets = [
    install_zerotier_hook
]