from setuptools import setup, find_packages
from os.path import join, dirname
import aur_upd

setup(
    name='aur_upd',
    include_package_data=True,
    description='Yet another AUR helper with a silent install/update capability',
    version=aur_upd.__version__,
    author='Vladimir Kamensky (aka MasterSoft24)',
    author_email='info@mastersoft24.ru ',
    packages=find_packages(),
    url="https://github.com/MasterSoft24/AUR_UPD",
    scripts=['aur_upd/bin/aur_update'],
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    long_description_content_type="text/markdown"
    # entry_points={
    #     'console_scripts': ['aur_upd=funniest.command_line:main'],
    # },
)