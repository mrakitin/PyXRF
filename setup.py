from setuptools import setup

import versioneer

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

requirements = ['setuptools'] + requirements

setup(
    name='pyxrf',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author='Brookhaven National Laboratory',
    url='https://github.com/NSLS-II/PyXRF',
    packages=['pyxrf', 'pyxrf.model', 'pyxrf.view', 'pyxrf.db_config', 'configs'],
    entry_points={'console_scripts': ['pyxrf = pyxrf.gui:run']},
    package_data={'pyxrf.view': ['*.enaml'], 'configs': ['*.json']},
    include_package_data=True,
    install_requires=requirements,
    python_requires='>=3.6',
    license='BSD',
    classifiers=['Development Status :: 3 - Alpha',
                 "License :: OSI Approved :: BSD License",
                 "Programming Language :: Python :: 3.6",
                 "Programming Language :: Python :: 3.7",
                 "Topic :: Software Development :: Libraries",
                 "Intended Audience :: Science/Research"]
)
