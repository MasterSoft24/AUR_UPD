from setuptools import setup, find_packages
from os.path import join, dirname
import aur_upd

setup(
    name='aur_upd',
    version=aur_upd.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
)