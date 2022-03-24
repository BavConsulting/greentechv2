from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in greentechv2/__init__.py
from greentechv2 import __version__ as version

setup(
	name="greentechv2",
	version=version,
	description="Greentech ERP ",
	author="Bav Systems",
	author_email="kedar.bavadekar@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
