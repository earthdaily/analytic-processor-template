from setuptools import find_packages, setup
with open('VERSION') as fh:
    version = fh.readline()

setup(
    name='{{ cookiecutter.project_slug }}',
    packages = find_packages('src'),
    package_dir={"":"src"},
    version=version,
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.author_name }}',
)
