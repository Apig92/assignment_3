'''
Created on 27 Feb 2017

@author: pigna
'''

import unittest
from src.main import led_grid

class Testgrid(unittest.TestCase):
   
    def test_on(self):
        t= led_grid(3)
        self.assertTrue(t.turn_on(0, 0, 2, 2)==[[True,True,True],[True,True,True],[True,True,True]])
        self.assertFalse(t.turn_on(0, 0, 2, 2)==[[True,False,True],[False,True,True],[True,True,True]])

    def test_off(self):
        t= led_grid(3)
        self.assertFalse(t.turn_off(0, 0, 2, 2)==[[True,True,True],[True,True,True],[True,True,True]])
        self.assertTrue(t.turn_off(0, 0, 2, 2)==[[False,False,False],[False,False,False],[False,False,False]])
        
    def test_switch(self):
        t= led_grid(3)
        t.turn_on(0, 0, 2, 2)
        self.assertTrue(t.switch(0, 0, 2, 2)==[[False,False,False],[False,False,False],[False,False,False]])
        self.assertTrue(t.switch(0, 0, 1, 1)==[[True,True,False],[True,True,False],[False,False,False]])
    
    def test_clean_up(self):
        t= led_grid(3)
        self.assertTrue(t.clean_up(-1, 1, 2, 13)[0]==0)
        self.assertTrue(t.clean_up(-1, 1, 2, 133)[3]==2)
        self.assertFalse(t.clean_up(-1, 1, 2, 2)[0]==-1)

    def test_execute(self):
        t= led_grid(3)
        self.assertTrue(t.execute_instructions("switch",0, 0, 1, 1)==[[True,True,False],[True,True,False],[False,False,False]])
        self.assertFalse(t.execute_instructions("turn on",0, 0, 2, 2)==[[False,False,False],[False,False,False],[False,False,False]])
        
    def test_count(self):
        t= led_grid(3)
        t.turn_on(0, 0, 2, 2)
        self.assertTrue(t.count_leds()==9)
        t.turn_off(0, 0, 2, 2) 
        self.assertTrue(t.count_leds()==0)
    
        
    

        

        


    
        
        
   
    