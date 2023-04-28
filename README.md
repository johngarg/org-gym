# org-gym

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/johngarg/org-gym/blob/master/LICENSE)

A tool for working with fitness data in emacs' org-mode.

## Installation

Install this tool using `pip`:

    pip install .

## Usage

For help, run:

    org-gym --help
    
The main command now is `parse`, e.g.

    org-gym parse ~/workouts.org

### Data files

The data files roughly follow the setup of [this similar project](https://github.com/guancio/org-fit). Workouts are primary headings with exercises as secondary TODO headings and each set is an element in an unordered list:

``` org
* Push workout
:PROPERTIES:
:date: 2023-01-01
:END:
** TODO Bench press
:PROPERTIES:
:muscle: chest
:note: pain in left shoulder
:END:
- 50 kg x 10
- 60 kg x 8
- 65 kg x 7
```

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd org-gym
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
