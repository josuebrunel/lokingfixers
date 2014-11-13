from setuptools import setup

with open('requirements.txt') as f:
            required = f.read().splitlines()

setup(
    name='lokingFixers',
    version='0.1',
    description='A simple toolbox to fix some usual issues on OSX and Linux',
    url='https://github.com/josuebrunel/lokingfixers',
    author='josue kouka',
    author_email='josuebrunel@gmail.com',
    license='MIT',
    package=['lokingfixers'],
    zip_safe=False,
    install_requires= required,
    scripts=['lokingfixers.py'],
)