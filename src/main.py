'''
Created on 27 Feb 2017

@author: pigna
'''

import urllib.request
import argparse
import re


def read_url(url):
    uri= url
    req = urllib.request.urlopen(uri)
    content = req.read().decode('utf-8').split("\n")
    array_size = content[0]
    instructions=[]
    for i in range(1,len(content)-1):
        pattern=re.compile("(turn on|turn off|switch)\s*,*\s*(-{0,1}\d+)\s*,*\s*(-{0,1}\d+)\s*through\s*(-{0,1}\d+)\s*,*\s*(-{0,1}\d+)")
        parsed_content=pattern.match(content[i]).groups()
        if parsed_content:
            instructions.append(parsed_content)
    return array_size,instructions

def read_instructions(command):
    pattern=re.compile("(turn on|turn off|switch)\s*(-{0,1}\d+),(-{0,1}\d+) through (-{0,1}\d+),(-{0,1}\d+)")
    parsed_content=pattern.match(command).group()
    instructions=[]
    if parsed_content:
        instructions.append(parsed_content)
    return instructions

class led_grid:
    def  __init__(self,size):
        self.size= size
        self.grid=[[False]*size for _ in range(0,size)]
                
    def turn_on(self,x1,y1,x2,y2):
        
        for i in range(y1,y2):
            for j in range(x1,x2):
                self.grid[i][j]=True
               
        return self.grid           
    
    def turn_off(self,x1,y1,x2,y2):
        for i in range(y1,y2):
            for j in range(x1,x2):
                self.grid[i][j]=False
        return self.grid  
    
    def switch(self,x1,y1,x2,y2):
        for i in range(y1,y2):
            for j in range(x1,x2):
                if self.grid[i][j]==True:
                    self.grid[i][j]=False
                elif self.grid[i][j]==False:
                    self.grid[i][j]=True
        
        return self.grid
               



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()
    urlname = args.input
    gridsize=read_url(urlname)[0]
    content=read_url(urlname)[1]
    c=led_grid(int(gridsize))
    oncounter=0
    offcounter=0
    switchcounter=0
    for i in range(len(content)):
        command,x1,y1,x2,y2=content[i][0],int(content[i][1]),int(content[i][2]),int(content[i][3]),int(content[i][4])
        if command=='turn on':
            oncounter+=1
            c.turn_on(x1,y1,x2,y2)

        elif command=='turn off':
            offcounter+=1
            c.turn_off(x1,y1,x2,y2)
           
        elif command=='switch':
            switchcounter+=1
            c.switch(x1,y1,x2,y2)
           
    print("on:",oncounter,"off:",offcounter,"Switch:",switchcounter)
       
    #for i in range(0,len(content)):
    #   print(content[i])
    
    print(c.grid[5])
    #print(c.grid[6])
    #c.switch(0,0,5,3)
        
        

if __name__ == '__main__':
    main()
    