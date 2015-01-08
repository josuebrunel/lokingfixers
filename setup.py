from setuptools import setup, find_packages

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
    # packages=[
    #     'lokingfixers', 
    #     'lokingfixers.fixers', 
    #     'lokingfixers.fixers.linux',
    #     'lokingfixers.fixers.osx',
    #     'lokingfixers.tools',
    #     'lokingfixers.models',
    # ],
    packages=find_packages(),
    zip_safe=False,
    install_requires= required,
    scripts=['lokingfixers.py'],
)