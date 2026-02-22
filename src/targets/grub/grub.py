from lbhelper import HookScript, StaticFile, download_file
from lbhelper import render_template_to_string, escape_string_for_shell_script
from lbhelper import render_template_to_file

from importlib.resources import files
from pathlib import Path

grub_theme_path = Path("/opt/grub_theme/theme.tar.gz")

# Patched calamares file
# https://salsa.debian.org/live-team/calamares-settings-debian-packaging/-/blob/master/helpers/calamares-bootloader-config?ref_type=heads
# Actual path
# https://packages.debian.org/sid/all/calamares-settings-debian/filelist
# Log will be under
# /root/.cache/calamares/session.log
calamares_grub_patch_content = escape_string_for_shell_script(
    render_template_to_string(
        template_path=Path(str(files(__package__) / "patch-calamares-grub.sh.j2")),
        grub_theme_path=grub_theme_path
    )
)

grub_theme_file = StaticFile(
    get_source_file=lambda: download_file("https://github.com/shvchk/poly-dark/archive/master.tar.gz"),
    target_filepath=grub_theme_path,
)

write_calamares_patch_hook = HookScript(
    get_script_file=lambda : render_template_to_file(
        Path(str(files(__package__) / "write-calamares-patch.sh.j2")),
        calamares_grub_patch_path=Path("/usr/share/calamares/helpers/calamares-bootloader-config"),
        calamares_grub_patch_content=calamares_grub_patch_content,
        grub_theme_path=grub_theme_path,
        grub_theme_dir_path=grub_theme_path.parent
    ),
    hook_name="patch-calamares",
    live_only=True,
)

targets = [
    grub_theme_file,
    write_calamares_patch_hook
]