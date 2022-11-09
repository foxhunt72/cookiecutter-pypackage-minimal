{{ cookiecutter.package_name }}
{{ cookiecutter.package_name|count * "=" }}


{{ cookiecutter.package_description }}

Version:
--------

{{ cookiecutter.package_version }}
For changes see [changelog]({{ cookiecutter.package_url }}/blob/main/CHANGELOG.md).


Usage
-----

```shellscript

  {{ cookiecutter.project_name }} --help

 

Installation
------------

```shellscript

  git clone {{ cookiecutter.package_url }}
  cd {{ cookiecutter.project_name }}
  pip3 install .

  pipx install {{ cookiecutter.package_name }}
  or
  pip3 install {{ cookiecutter.package_name }}


### Requirements

- package1
- package2

Compatibility
-------------

Licence
-------
{{ cookiecutter.open_source_license }}

Authors
-------
{{ cookiecutter.author_name }}

[{{ cookiecutter.package_name }}]({{ cookiecutter.package_url }}) was written by [{{ cookiecutter.author_name }}]({{ cookiecutter.author_email }}).

