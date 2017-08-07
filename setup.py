import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="libnotify-terminal",
    version="0.4.0",
    author="SolarLiner",
    author_email="solarliner@gmail.com",
    description="A binary tool to send notification",
    long_description=read("README.md"),
    license="MIT",
    keywords="gobject libnotify linux notifications",
    packages=find_packages(exclude=['tests', '.vscode']),
    install_requires=['gobject', 'notify2'],
    entry_points={
        'console_scripts': {
            'libnotify-terminal=libnotify_terminal:main'
        }
    }
)