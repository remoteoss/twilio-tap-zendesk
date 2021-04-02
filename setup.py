#!/usr/bin/env python

from setuptools import setup

setup(name='bmaquet-tap-zendesk',
      version='1.5.4',
      description='Singer.io tap for extracting data from the Zendesk API',
      author='Stitch',
      url='https://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['bmaquet_tap_zendesk'],
      install_requires=[
          'pipelinewise-singer-python==1.2.0',
          'zenpy==2.0.13',
      ],
      extras_require={
          'dev': [
              'ipdb',
              'pylint',
              'nose',
              'nose-watch',
          ]
      },
      entry_points='''
          [console_scripts]
          bmaquet-tap-zendesk=bmaquet_tap_zendesk:main
      ''',
      packages=['bmaquet_tap_zendesk'],
      include_package_data=True,
)
