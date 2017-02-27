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



n=10
a=[[0]*n for _ in range(n)]
print(a[2:5])


'''
class led_grid:
    def turn_on(self,i,j):
        pass
    def turn_off(self,i,j):
        pass
    def switch(self,i,j):
        pass
'''

if __name__ == '__main__':
    pass