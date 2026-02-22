from pathlib import Path
from importlib.resources import files
import settings

from lbhelper import HookScript, render_template_to_file, render_template_to_string, \
    escape_string_for_shell_script, StaticFile

obsidian_install_path = settings.CUSTOM_APP_BASE_DIR / "obsidian" / "obsidian.AppImage"
obsidian_entry_path = settings.DESKTOP_ENTRY_DIR / "obsidian.desktop"
obsidian_icon_path = settings.CUSTOM_APP_BASE_DIR / "obsidian" / "obsidian.svg"

obsidian_entry_content = escape_string_for_shell_script(
    render_template_to_string(
        Path(str(files(__package__) / "obsidian.desktop.j2")),
        obsidian_install_path=obsidian_install_path,
        obsidian_icon_path=obsidian_icon_path,
    )
)

install_obsidian_hook = HookScript(
    get_script_file=lambda : render_template_to_file(
        Path(str(files(__package__) / "install-obsidian.sh.j2")),
        obsidian_install_dir_path=obsidian_install_path.parent,
        obsidian_install_path=obsidian_install_path,
        obsidian_entry_path=obsidian_entry_path,
        obsidian_entry_content=obsidian_entry_content,
    ),
    hook_name="install-obsidian",
)

obsidian_icon_file = StaticFile(
    get_source_file=lambda: Path(str(files(__package__) / "obsidian.svg")),
    target_filepath=obsidian_icon_path,
)

targets = [
    install_obsidian_hook,
    obsidian_icon_file,
]