#!/usr/bin/env python
from setuptools import setup
import versioneer

setup(name='pv_soiling',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='A package for extracting soiling of PV sites',
      license='MIT',
      author='Michael Deceglie',
      author_email="michael.deceglie@nrel.gov",
      url='https://github.com/NREL/pv_soiling',
      packages=['pv_soiling'],
      install_requires=["pandas", "numpy", "scipy"],
      )
