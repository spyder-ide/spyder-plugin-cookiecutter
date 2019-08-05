# Spyder Plugin Cookiecutter

## Project details
[![Join the chat at https://gitter.im/spyder-ide/public](https://badges.gitter.im/spyder-ide/spyder.svg)](https://gitter.im/spyder-ide/public)
[![OpenCollective Backers](https://opencollective.com/spyder/backers/badge.svg?color=blue)](#backers)
[![OpenCollective Sponsors](https://opencollective.com/spyder/sponsors/badge.svg?color=blue)](#sponsors)

## Build status
[![CircleCI](https://circleci.com/gh/spyder-ide/spyder-plugin-cookiecutter.svg?style=svg)](https://circleci.com/gh/spyder-ide/spyder-plugin-cookiecutter)


## Overview

Powered by [Cookiecutter](https://github.com/audreyr/cookiecutter) :cookie:, Spyder Plugin Cookiecutter is a template for jumpstarting [Spyder IDE](https://github.com/spyder-ide/spyder) :spider_web: plugins quickly.

> We recommend using conda and anaconda when developing a Spyder-IDE plugin.

## Features

- Compatible with Spyder >=3.1 and Spyder 4
- Follows Spyder Plugin Structure (`plugin.py`, `widgets`, `assets`, `tests`)
- A functional basic plugin.

### Repo structure
- `License.txt`, `MANIFIEST.in`, `CONTRIBUTORS.md` and `.gitatributes`
- `README.rst` with bagdes and some instructions.

### Packaging

- `requirements.txt` file for easy install dependencies for development
- `setup.py`
- Recipe files for creating conda package.

### Testing and Continuous Integration

- pytest configuration, and a basic test
- Integration with [Appveyor](https://www.appveyor.com/) for windows testing.
- Integration with [Circle-CI](https://circleci.com/) for linux testing.

### Code Checking

- Test Coverage with [Coveralls](https://coveralls.io/) Integration.
- Integration with [ciocheck](https://github.com/ContinuumIO/ciocheck/) for linting and codestyle checking
- Integration with [Scrutinizer CI](https://scrutinizer-ci.com/) for Code Quality


## Usage

First, get Cookiecutter:

```
$ conda install "cookiecutter>=1.4.0"
```

Now run against the repo:

```
$ cookiecutter gh:spyder-ide/spyder-plugin-cookiecutter
```

You'll be prompted for some values. and after that the repo will be generated

Normally you don't need to change `python_package_name` and `git_repo_name`.

Example:

```
plugin_name [Demo]: 
git_repo_name [spyder-demo]: 
python_package_name [spyder_demo]: 
description [Plugin for Spyder IDE.]: 
version [0.1.0]: 
author [Spyder Project Contributors]: 
email [admin@spyder-ide.org]: 
github_username [spyder-ide]:
graphical_plugin [y]: 
create_config_page [n]: 
support_python_2 [n]: 
spyder3_compatibility [n]: 
```

## Testing

For testing you need to install pytest and pytest-cookies

```
$ pip install pytest pytest-cookies
```

And run pytest:

```
$ pytest
```

## Contributing

Everyone is welcome to contribute!

## Backers

Support us with a monthly donation and help us continue our activities.

[![Backers](https://opencollective.com/spyder/backers.svg)](https://opencollective.com/spyder#support)

## Sponsors

Become a sponsor to get your logo on our README on Github.

[![Sponsors](https://opencollective.com/spyder/sponsors.svg)](https://opencollective.com/spyder#support)
