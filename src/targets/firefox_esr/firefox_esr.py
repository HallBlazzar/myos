from lbhelper import StaticFile, HookScript, download_file, render_template_to_file, render_template_to_string

from importlib.resources import files
from pathlib import Path

# Refer to https://support.mozilla.org/en-US/kb/customizing-firefox-using-policiesjson
firefox_esr_config_path = Path("/usr/lib/firefox-esr/distribution/policies.json")
extension_dir = Path("/opt/firefox-esr/extensions")
policy_path = Path("/usr/share/firefox-esr/distribution/policies.json")

workona_path = extension_dir / "workona.xpi"
undo_tab_path = extension_dir / "undo.xpi"

undo_tab_extension = StaticFile(
    undo_tab_path,
    get_source_file=lambda : download_file(undo_tab_url),
)

firefox_esr_policy_content = render_template_to_string(
    template_path=Path(str(files(__package__) / "policies.json.j2")),
    extensions=[workona_path, undo_tab_path]
)

firefox_esr_extension_installation_hook = HookScript(
    get_script_file=lambda : render_template_to_file(
        template_path=Path(str(files(__package__) / "install-extension.sh.j2")),
        extension_dir_path=extension_dir,
        policy_content=firefox_esr_policy_content,
        policy_dir_path=policy_path.parent,
        policy_path=policy_path,
    ),
    hook_name="install-firefox-esr-extensions",
)

firefox_esr_autoconfig_path = Path("/etc/firefox-esr/firefox-esr.js")

firefox_esr_autoconfig_file = StaticFile(
    firefox_esr_autoconfig_path,
    get_source_file=lambda : Path(str(files(__package__) / "firefox-esr.js"))
)

targets = [
    firefox_esr_extension_installation_hook,
    firefox_esr_autoconfig_file,
]
