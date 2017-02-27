'''
Created on 27 Feb 2017

@author: pigna
'''
'''

Ideas for the code
Read list, get size of the grid.

Initialise to 0 every cell.


3 functions:turn on, turn off, switch


def on(grid)
     for i in range (set by interval wanted)
      for j n range (set by interval wanted)
        if grid[i,j]!= on
            change element to on
        else
            leave on

def off(grid) Same thing, but off



def switch(grid)
    for i in range (set by interval wanted)
      for j n range (set by interval wanted)
        if grid[i,j]== on
            change element to off
        elif grid[i,j]==off
            change element to off
        else
            print(there is an error in this coordinate)
'''
import urllib.request
uri = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
req = urllib.request.urlopen(uri)
buffer = req.read().decode('utf-8')





class led_grid:
    def  __init__(self,size):
        self.size= size
        self.grid=[[False]*size for _ in range(0,size)]
        print(self.grid)
                
    def turn_on(self):
        
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j]==False:
                    self.grid[i][j]=True
               
        print(self.grid)  
               
    
    def turn_off(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j]==True:
                    self.grid[i][j]=False
               
        print(self.grid)  
    
    def switch(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j]==True:
                    self.grid[i][j]=False
                elif self.grid[i][j]==False:
                    self.grid[i][j]=True
               
        print(self.grid)
        
        

if __name__ == '__main__':
    
    c=led_grid(3)
    c.turn_on()
    c.turn_off()
    c.switch()
    c.switch()
    c.turn_off()
    