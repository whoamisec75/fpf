import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "fpf",
    version = "1.1",
    author = "Devansh Raghav",
    author_email = "whoamisec75@gmail.com",
    license = "MIT",
    keywords = ["fpf", "Bug Bounty", "pentesting", "security", "hacking"],
    url = "https://github.com/DevanshRaghav75/fpf",
    packages=find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
    install_requires=[
        'colorama',
    ],

    entry_points={
        'console_scripts': [
            'fpf = fpf.__main__:executor'
        ]
    },
)
