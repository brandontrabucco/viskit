"""Setup script for viskit."""

from setuptools import find_packages
from setuptools import setup


REQUIRED_PACKAGES = ['Flask==1.0.2', 'matplotlib==2.0.2', 'plotly==3.4.2', 'numpy==1.11.3']

setup(name='viskit',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    include_package_data=True,
    packages=[p for p in find_packages() if p.startswith('viskit')],
    description="rllab's viskit with some added features")