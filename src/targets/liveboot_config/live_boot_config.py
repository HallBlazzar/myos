from lbhelper import StaticFile
from pathlib import Path
from importlib.resources import files

# https://manpages.debian.org/unstable/live-config-doc/live-config.7.en.html#live~12
liveboot_config_path = Path("/etc/live/config.conf.d/10-user-setup.conf")

liveboot_config_file = StaticFile(
    target_filepath=liveboot_config_path,
    get_source_file=lambda : Path(str(files(__package__) / "10-user-setup.conf")),
)

targets = [
    liveboot_config_file,
]