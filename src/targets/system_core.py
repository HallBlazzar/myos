from lbhelper import UpstreamPackages

core_packages = UpstreamPackages(
    packages=[
        "coreutils",
        "memtest86+",
    ],
    package_set_code="core-packages",
)

targets = [
    core_packages,
]
