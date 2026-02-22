from lbhelper import build_image
from targets import targets
from pathlib import Path


if __name__ == '__main__':
    build_image(targets=targets, iso_build_dir=Path("build"))
