from lbhelper import UpstreamPackages, HookScript
from lbhelper import AptPreference, AptPreferenceType
from lbhelper import render_template_to_file
from importlib.resources import files
from pathlib import Path

dconf_path = Path("/etc/dconf/db/local.d/00-extensions")
dconf_profile_path = Path("/etc/dconf/profile/user")

gnome_desktop_packages = UpstreamPackages(
    packages=[
        "dconf-editor",
        "task-gnome-desktop",
        "task-english",
    ],
    package_set_code="desktop",
)

core_gnome_extensions_packages = UpstreamPackages(
    packages=[
        "gnome-shell-extension-manager",
        # "gnome-shell-extension-dashtodock",

        # AppIndicator related packages
        "gnome-shell-extension-appindicator",
        "libayatana-appindicator3-1",

        "gnome-shell-extension-kimpanel",
        # "gnome-shell-extension-status-icons",
        # for vital
        "gir1.2-gtop-2.0"
    ],
    package_set_code="core-gnome-extensions",
)

install_extensions_hook = HookScript(
    get_script_file=lambda : Path(str(files(__package__) / "install-extensions.sh")),
    hook_name="install-gnome-extensions",
)

# see https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/desktop_migration_and_administration_guide/extensions-enable
adjust_default_gsettings_hook = HookScript(
    get_script_file=lambda : render_template_to_file(
        Path(str(files(__package__) / "adjust-default-gsettings.sh.j2")),
        dconf_dir_path=dconf_path.parent,
        dconf_path=dconf_path,
        dconf_profile_path=dconf_profile_path
    ),
    hook_name="adjust-default-gsettings",
)

omit_desktop_apps = AptPreference(
    package="libroffice",
    pin="version *",
    pin_priority=-1,
    preference_type=AptPreferenceType.RUN_TIME
)

targets = [
    gnome_desktop_packages,
    core_gnome_extensions_packages,
    install_extensions_hook,
    adjust_default_gsettings_hook,
    omit_desktop_apps
]
