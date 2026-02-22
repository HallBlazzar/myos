from lbhelper import UpstreamPackages, HookScript
from pathlib import Path
from importlib.resources import files


plymouth_animation_packages = UpstreamPackages(
    packages=[
        "plymouth",
        "plymouth-x11",
        "plymouth-themes",
    ],
    package_set_code="boot-animation",
)

plymouth_theme_hook = HookScript(
    get_script_file=lambda : Path(str(files(__package__) / "plymouth-theme.sh")),
    hook_name="plymouth_theme",
)

targets = [
    plymouth_animation_packages,
    plymouth_theme_hook,
]