from pathlib import Path
from importlib.resources import files

from lbhelper import UpstreamPackages, StaticFile, HookScript, render_template_to_file, \
    render_template_to_string, escape_string_for_shell_script

default_oh_my_zsh_installation_path = Path("/etc/skel/.oh-my-zsh")
default_starship_config_path = Path("/etc/skel/.config/starship.toml")
default_zsh_config_path = Path("/etc/skel/.zshrc")

shell_packages = UpstreamPackages(
    packages=[
        "zsh",
        "starship",
        "lsd",
    ],
    package_set_code="core-tools",
)

# Based on https://stackoverflow.com/questions/31624649/how-can-i-get-a-secure-system-wide-oh-my-zsh-configuration/42193058#42193058
install_on_my_zsh_hook = HookScript(
    get_script_file=lambda :render_template_to_file(
        Path(str(files(__package__) / "install-oh-my-zsh.sh.j2")),
        oh_my_zsh_installation_path=default_oh_my_zsh_installation_path
    ),
    hook_name="install-oh-my-zsh",
)

# For global install - https://zsh.sourceforge.io/Doc/Release/Files.html#Startup_002fShutdown-Files
zshrc_file = StaticFile(
    target_filepath=default_zsh_config_path,
    get_source_file=lambda :Path(str(files(__package__) / ".zshrc")),
)

starship_config = StaticFile(
    target_filepath=default_starship_config_path,
    get_source_file=lambda : Path(str(files(__package__) / "starship.toml")),
)

# See - https://github.com/calamares/calamares/blob/calamares/src/modules/users/users.conf
calamares_default_shell_patch_path = Path("/etc/calamares/modules/users.conf")

calamares_default_shell_patch_content = escape_string_for_shell_script(
    render_template_to_string(
        template_path=Path(str(files(__package__) / "patch-calamares-default-shell.sh")),
    )
)

calamares_default_shell_patch_hook = HookScript(
    get_script_file=lambda : render_template_to_file(
        Path(str(files(__package__) / "write-calamares-patch.sh.j2")),
        calamares_default_shell_patch_path=calamares_default_shell_patch_path,
        calamares_default_shell_patch_content=calamares_default_shell_patch_content,
    ),
    hook_name="patch-calamares-default-shell",
    live_only=True,
)

targets = [
    shell_packages,
    install_on_my_zsh_hook,
    zshrc_file,
    starship_config,
    calamares_default_shell_patch_hook,
]