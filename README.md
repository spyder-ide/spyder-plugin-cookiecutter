# Spyder Plugin Cookiecutter

[![CircleCI](https://circleci.com/gh/spyder-ide/spyder-plugin-cookiecutter.svg?style=svg)](https://circleci.com/gh/spyder-ide/spyder-plugin-cookiecutter)

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

### Repo Managing

- (Optional) Version managing with  [versioneer](https://github.com/warner/python-versioneer)


## Usage

First, get Cookiecutter:

```
$ conda install "cookiecutter>=1.4.0"
```

If you want to use versioneer: (also you need to install git)

```
$ conda install versioneer
```

Now run against the repo:

```
$ cookiecutter gh:spyder-ide/spyder-plugin-cookiecutter
```

You'll be prompted for some values. and after that the repo will be generated

Normally you don't need to change `project_name` and `repo_name`.

Example:

```
author [Spyder Project Contributors]:
email [admin@spyder-ide.org]:
github_username [spyder-ide]:
plugin_name [Demo Plugin]: Reports
repo_name [spyder-reports]:
project_name [spyder_reports]:
description [Plugin for Spyder IDE.]: Spyder Plugin for Markdown reports for Pweave
version [0.1.0]:
create_config_page [n]:
use_ciocheck [y]:
support_python_2 [n]:
spyder3_compatibility [y]:
use_versioneer [y]:
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
