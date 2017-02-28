'''
Created on 27 Feb 2017

@author: pigna
'''

import urllib.request
import argparse

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()
    filename = args.input
    return filename

def read_url(url):
    uri= url
    req = urllib.request.urlopen(uri)
    buffer = req.read().decode('utf-8').split("\n")
    array_size = buffer[0]
    commands= buffer[1:]
    return array_size,commands

class led_grid:
    def  __init__(self,size):
        self.size= size
        self.grid=[[False]*size for _ in range(0,size)]
                
    def turn_on(self,x1,y1,x2,y2):
        
        for i in range(y1,y2):
            for j in range(x1,x2):
                self.grid[i][j]=True
               
            print(self.grid[0])  
               
    
    def turn_off(self,x1,y1,x2,y2):
        for i in range(y1,y2):
            for j in range(x1,x2):
                self.grid[i][j]=False
               
                print(self.grid[0])    
    
    def switch(self,x1,y1,x2,y2):
        for i in range(y1,y2):
            for j in range(x1,x2):
                if self.grid[i][j]==True:
                    self.grid[i][j]=False
                elif self.grid[i][j]==False:
                    self.grid[i][j]=True
               



def main():
    filename=read_url(parse())[0]
    c=led_grid(int(filename))
    c.turn_on(1,0,999,2)
    c.switch(0,0,5,3)
        
        

if __name__ == '__main__':
    main()
    