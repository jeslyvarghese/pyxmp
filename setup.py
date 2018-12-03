from setuptools import setup
import sys

import pyxmp

sys.path.append('./pyxmp')
sys.path.append('./tests')

with open("README.rst", "r") as f:
    description = f.read()

setup(
    name = "pyxmp",
    version = piexif.VERSION,
    author = "egghese",
    author_email = "justin@redatomize.com",
    description = "An xmp library purely written in python",
    long_description = description,
    license = "MIT",
    keywords = ["xmp", "jpeg"],
    url = "https://github.com/jeslyvarghese/pyxmp",
    packages = ['pyxmp'],
    test_suite = 's_test.suite',
    classifiers = [
        "Development Status :: 5 - Development/Unstable",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: IronPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "License :: OSI Approved :: MIT License",
        "Topic :: Multimedia",
        "Topic :: Printing",
    ]
)
