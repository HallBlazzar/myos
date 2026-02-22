from lbhelper import UpstreamPackages

core_tools_packages = UpstreamPackages(
    packages=[
        "curl",
        "git",
        "gnupg",
        "dpkg-dev",
        "dbus-x11",
        # for AppImages
        "libfuse2t64",
        "jq",
        "yq",
        "task-ssh-server",
        "vim",
    ],
    package_set_code="core-tools",
)

desktop_tools_packages = UpstreamPackages(
    packages=[
        "nm-connection-editor",
        "alacarte",
        "ptyxis",
        "gedit",
        "pcmanfm",
        "wireshark",
    ],
    package_set_code="desktop-tools",
)

vm_packages = UpstreamPackages(
    packages=[
        "qemu-system",
        "libvirt-daemon-system",
        "libvirt-clients",
        "bridge-utils",
        "virt-manager",
        "libvirt-dev",
        "ebtables",
        "libguestfs-tools",
        "ruby-fog-libvirt",
        # required by vagrant
        "nfs-common"
    ],
    package_set_code="vm",
)

run_in_vm_packages = UpstreamPackages(
    packages=[
        "virtualbox-guest-additions-iso",
        "spice-vdagent",
        "qemu-guest-agent",
    ],
    package_set_code="run-in-vm",
    live_only=True,
)

container_packages = UpstreamPackages(
    packages=[
        "distrobox"
    ],
    package_set_code="container",
)

# https://developer.android.com/studio/install#64bit-libs
# https://developer.android.com/studio/run/emulator-acceleration
android_studio_dependencies_packages = UpstreamPackages(
    packages=[
        "cpu",
        "lib32z1",
        "libbz2-1.0",
        "libstdc++6",
        "libncursesw6",
        "libncurses6",
        "ncurses-base",
        "ncurses-bin",
        "ncurses-term",
    ],
    package_set_code="android-studio-dep",
)

targets = [
    core_tools_packages,
    desktop_tools_packages,
    vm_packages,
    run_in_vm_packages,
    container_packages,
    android_studio_dependencies_packages,
]