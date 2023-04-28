# org-gym

[![PyPI](https://img.shields.io/pypi/v/org-gym.svg)](https://pypi.org/project/org-gym/)
[![Changelog](https://img.shields.io/github/v/release/johngarg/org-gym?include_prereleases&label=changelog)](https://github.com/johngarg/org-gym/releases)
[![Tests](https://github.com/johngarg/org-gym/workflows/Test/badge.svg)](https://github.com/johngarg/org-gym/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/johngarg/org-gym/blob/master/LICENSE)

A tool for working with fitness data in orgmode.

## Installation

Install this tool using `pip`:

    pip install org-gym

## Usage

For help, run:

    org-gym --help

You can also use:

    python -m org_gym --help

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd org-gym
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
