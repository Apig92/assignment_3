'''
Created on 30 Jan 2017

@author: pigna
'''
from setuptools import setup

setup(name="led_tester",
      version="0.1",
      description="Assignment 3, COMP30670. It tests LEDs on a square grid.",
      url="",
      author="Andrea Pignanelli",
      author_email="andrea.pignanelli01@ucdconnect.ie",
      licence="GPL3",
      packages=['a3'],
      entry_points={
          'console_scripts':['solve_led=a3.main:main']
          },
      install_requires=[
          'numpy',
        ],
    )