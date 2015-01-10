import os
from setuptools import setup, find_packages

def build_dir_path(dirname):
            return os.path.join(os.path.expanduser('~'),dirname)

with open('requirements.txt') as f:
            required = f.read().splitlines()

pkg_cfg_dir = build_dir_path('.lokingfixers')
pkg_cfg_subdir = build_dir_path('.lokingfixers/logs')
            
setup(
    name='lokingFixers',
    version='0.1',
    description='A simple toolbox to fix some usual issues on OSX and Linux',
    url='https://github.com/josuebrunel/lokingfixers',
    author='josue kouka',
    author_email='josuebrunel@gmail.com',
    license='MIT',
    packages=find_packages(),
    #package_date={'': ['requirements.txt']},
    include_package_data=True,
    data_files = [
       (pkg_cfg_dir, []),
       (pkg_cfg_subdir, []),
       (pkg_cfg_dir, ['lokingfixers/settings.py'])
    ],
    zip_safe=False,
    install_requires=required,
    scripts=['lokingfixer.py'],
)
