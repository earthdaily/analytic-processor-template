from setuptools import find_packages, setup

setup(
    name='{{ cookiecutter.project_slug }}',
    packages = find_packages('src'),
    package_dir={"":"src"},
    version="0.0.1",
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.author_name }}',
)
