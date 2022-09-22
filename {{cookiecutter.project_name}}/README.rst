{{ cookiecutter.package_name }}
{{ cookiecutter.package_name|count * "=" }}


{{ cookiecutter.package_description }}

Usage
-----

Installation
------------

.. code-block:: bash

  git clone {{ cookiecutter.package_url }}
  cd {{ cookiecutter.project_name }}
  pip3 install .

  pipx install {{ cookiecutter.package_name }}
  or
  pip3 install {{ cookiecutter.package_name }}


Requirements
^^^^^^^^^^^^
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

`{{ cookiecutter.package_name }}` was written by `{{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>`_.
