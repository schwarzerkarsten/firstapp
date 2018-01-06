from setuptools import setup, find_packages

setup(
        name = "firstapp",
        version = "0.1",
        description = "My first os app",
        packages = find_packages(),
        install_requires = ["gunicorn"],
        )
