'''
Created on 30 Jan 2017

@author: pigna
'''

from setuptools import setup

setup(name="systeminfo",
      version="0.1",
      description="Basic system information for COMP30670",
      url="",
      author="ME",
      author_email="andrea.pignanelli01@ucdconnect.ie",
      licence="GPL3",
      packages=['a3'],
      entry_points={
          'console_scripts':['comp30670_systeminfo=a3.main:main']
          }
    )