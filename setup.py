from setuptools import setup, find_packages

setup(
    name='mycli',
    version='0.1.0',
    packages=find_packages(),
    install_requires=["typer"],
    entry_points={
        'console_scripts': [
            'mycli = mycli.cli:app',
        ],
    },
)