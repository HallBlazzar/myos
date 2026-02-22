from lbhelper import UpstreamPackages


live_installer_packages = UpstreamPackages(
    packages=[
        "calamares",
        "calamares-settings-debian",
    ],
    package_set_code="live_installer",
    live_only=True,
)

targets = [
    live_installer_packages,
]