{{ cookiecutter.plugin_name }}
======

Build status
------------
|travis status| |appveyor status| |circleci status| |coverage| |quantified code| |scrutinizer|

Project information
-------------------
|license| |pypi version| |gitter|

.. |travis status| image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master.svg
  :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
  :alt: Travis-CI build status
.. |appveyor status| image:: https://img.shields.io/appveyor/ci/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master.svg
  :target: https://ci.appveyor.com/project/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
  :alt: Appveyor build status
.. |circleci status| image:: https://img.shields.io/circleci/project/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master.svg
  :target: https://circleci.com/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/tree/master
  :alt: Circle-CI build status
.. |quantified code| image:: https://www.quantifiedcode.com/api/v1/project/PROJECT_ID/badge.svg
  :target: https://www.quantifiedcode.com/app/project/PROJECT_ID
  :alt: Quantified Code issues
.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg
  :target: https://scrutinizer-ci.com/g/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/?branch=master
  :alt: Scrutinizer Code Quality
.. |license| image:: https://img.shields.io/pypi/l/{{ cookiecutter.repo_name }}.svg
  :target: LICENSE.txt
  :alt: License
.. |pypi version| image:: https://img.shields.io/pypi/v/{{ cookiecutter.repo_name }}.svg
  :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}
  :alt: Latest PyPI version
.. |gitter| image:: https://badges.gitter.im/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg
  :target: https://gitter.im/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
  :alt: Join the chat at https://gitter.im/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
.. |coverage| image:: https://coveralls.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/badge.svg
  :target: https://coveralls.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}?branch=master
  :alt: Code Coverage


Description
-----------
{{ cookiecutter.description }}.

Installation
------------

Using pip

::

pip install {{ cookiecutter.project_name }}

Using conda

::

conda install {{ cookiecutter.project_name }} -c spyder-ide

Usage
-----

