from lbhelper import UpstreamPackages

thunderbolt_packages = UpstreamPackages(
    packages=[
        "thunderbolt-tools",
        "bolt",
    ],
    package_set_code="thunderbolt"
)

video_packages = UpstreamPackages(
    packages=[
        "gstreamer1.0-vaapi",
    ],
    package_set_code="video"
)

amd_driver_packages = UpstreamPackages(
    packages=[
        "i965-va-driver",
        "firmware-amd-graphics",
    	"libgl1-mesa-dri",
	    "libglx-mesa0",
	    "libegl1-mesa-dev",
	    "libegl-mesa0",
        "libglu1-mesa",
        "mesa-vulkan-drivers",
        "mesa-utils",
        "mesa-utils-bin",
        "mesa-va-drivers",
        "xserver-xorg-video-all",
        "radeontop",
    ],
    package_set_code="amd-driver"
)

dell_driver_packages = UpstreamPackages(
    packages=[
        "firmware-realtek",
        "firmware-mediatek"
    ],
    package_set_code="dell-driver"
)

pcie_packages = UpstreamPackages(
    packages=[
        "pciutils",
    ],
    package_set_code="pci"
)

linux_firmware_packages = UpstreamPackages(
    packages=[
        "firmware-linux",
    ],
    package_set_code="firmware-linux"
)

laptop_packages = UpstreamPackages(
    packages=[
        "task-laptop",
    ],
    package_set_code="laptop"
)

targets = [
    thunderbolt_packages,
    video_packages,
    amd_driver_packages,
    dell_driver_packages,
    pcie_packages,
    linux_firmware_packages,
    laptop_packages
]