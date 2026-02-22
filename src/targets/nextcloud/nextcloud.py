from pathlib import Path
from importlib.resources import files
import settings

from lbhelper import HookScript, render_template_to_file, render_template_to_string, \
    escape_string_for_shell_script, StaticFile

nextcloud_install_path = settings.CUSTOM_APP_BASE_DIR / "nextcloud" / "nextcloud.AppImage"
nextcloud_entry_path = settings.DESKTOP_ENTRY_DIR / "nextcloud.desktop"
nextcloud_icon_path = settings.CUSTOM_APP_BASE_DIR / "nextcloud" / "nextcloud.svg"

nextcloud_entry_content = escape_string_for_shell_script(
    render_template_to_string(
        Path(str(files(__package__) / "nextcloud.desktop.j2")),
        nextcloud_install_path=nextcloud_install_path,
        nextcloud_icon_path=nextcloud_icon_path,
    )
)

install_nextcloud_hook = HookScript(
    get_script_file=lambda : render_template_to_file(
        Path(str(files(__package__) / "install-nextcloud.sh.j2")),
        nextcloud_install_dir_path=nextcloud_install_path.parent,
        nextcloud_install_path=nextcloud_install_path,
        nextcloud_entry_path=nextcloud_entry_path,
        nextcloud_entry_content=nextcloud_entry_content,
    ),
    hook_name="install-nextcloud",
)

nextcloud_icon = StaticFile(
    get_source_file=lambda: Path(str(files(__package__) / "nextcloud.svg")),
    target_filepath=nextcloud_icon_path,
)

targets = [
    install_nextcloud_hook,
    nextcloud_icon
]