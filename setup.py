from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="org-gym",
    description="A tool for working with fitness data in emacs' org-mode.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="John Gargalionis",
    url="https://github.com/johngarg/org-gym",
    project_urls={
        "Issues": "https://github.com/johngarg/org-gym/issues",
        "CI": "https://github.com/johngarg/org-gym/actions",
        "Changelog": "https://github.com/johngarg/org-gym/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["org_gym"],
    entry_points="""
        [console_scripts]
        org-gym=org_gym.cli:cli
    """,
    install_requires=["click"],
    extras_require={
        "test": ["pytest"]
    },
    python_requires=">=3.7",
)
