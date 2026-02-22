from lbhelper import HookScript, StaticFile, UpstreamPackages
from pathlib import Path
from importlib.resources import files


install_fcitx5_hook = HookScript(
    get_script_file=lambda : Path(str(files(__package__) / "install-fcitx5.sh")),
    hook_name="install-fcitx5",
)

fcitx5_config_var = StaticFile(
    get_source_file=lambda : Path(str(files(__package__) / "fcitx5-config")),
    target_filepath=Path("/etc/skel/.var/app/org.fcitx.Fcitx5/config/fcitx5")
)

fcitx5_config = StaticFile(
    get_source_file=lambda : Path(str(files(__package__) / "fcitx5-config")),
    target_filepath=Path("/etc/skel/.config/fcitx5")
)

fcitx5_config_panel_package = UpstreamPackages(
    packages=["fcitx5-config-qt"],
    package_set_code="fcitx5-configtool",
)

targets = [
    install_fcitx5_hook,
    fcitx5_config,
    fcitx5_config_var,
    fcitx5_config_panel_package,
]