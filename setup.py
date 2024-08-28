"""Python setup.py for music_manager package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("music_manager", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="music_manager",
    version=read("music_manager", "VERSION"),
    description="Awesome music_manager created by HritwikSinghal",
    url="https://github.com/HritwikSinghal/music_manager/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="HritwikSinghal",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["music_manager = music_manager.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
