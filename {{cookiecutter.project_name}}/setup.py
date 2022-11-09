import io
import os
import re

from setuptools import find_packages
from setuptools import setup


about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'src', '{{cookiecutter.package_name}}', '__version__.py')) as f:
    exec(f.read(), about)


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


with open("./requirements.txt") as requirements:
    REQUIREMENTS = requirements.read().splitlines()

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}


setup(
    name="{{ cookiecutter.project_name }}",
    version=about["__version__"],
    url="{{ cookiecutter.package_url }}",
    license="{{ cookiecutter.open_source_license }}",
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",
    description="{{ cookiecutter.package_description }}",
    long_description=read("README.md"),
    long_description_content_type='text/markdown',
    {%- if 'no' not in cookiecutter.command_line_interface|lower %}
    entry_points={
        "console_scripts": [
            "{{ cookiecutter.project_name }}={{ cookiecutter.package_name }}.cli:main",
        ],
    },
    {%- endif %}

    packages=find_packages(
        where="src",
        exclude=(
            "tests",
            "tests_*",
        )
    ),
    package_dir={"": "src"},
    install_requires=REQUIREMENTS,
    classifiers=[
        "{{ cookiecutter.development_status }}",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)

