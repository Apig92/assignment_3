'''
Created on 30 Jan 2017

@author: pigna
'''
from setuptools import setup

setup(name="solveled",
      version="0.2",
      description="Assignment 3, COMP30670. It tests LEDs on a square grid.",
      url="",
      author="Andrea Pignanelli",
      author_email="andrea.pignanelli01@ucdconnect.ie",
      licence="GPL3",
      packages=['src'],
      entry_points={
          'console_scripts':['solveled=src.main:main']
          },
      install_requires=[
          'numpy',
        ],
    )