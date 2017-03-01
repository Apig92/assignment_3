'''
Created on 27 Feb 2017

@author: pigna
'''
import urllib.request
import argparse
import re
import time
start_time = time.time()

def read_url():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()
    urlname = args.input
    uri= urlname
    req = urllib.request.urlopen(uri)
    content = req.read().decode('utf-8').split("\n")
    array_size = content[0]
    instructions=[]
    for i in range(1,len(content)-1):
        pattern=re.compile("\s*(turn on|turn off|switch)\s*,*\s*(-{0,1}\d+)\s*,*\s*(-{0,1}\d+)\s*through\s*(-{0,1}\d+)\s*,*\s*(-{0,1}\d+)")
        if pattern.match(content[i]) != None:
            parsed_content=pattern.match(content[i]).groups()
            instructions.append(parsed_content)
    return array_size,instructions,urlname

def clean_up(gridsize,x1,y1,x2,y2):
    if x1<0:
        x1=0
    if x2<0:
        x2=0   
    if x2>(int(gridsize)-1):
        x2=int(gridsize)-1
    if x1>(int(gridsize)-1):
        x1=int(gridsize)-1    
    if y1<0:
        y1=0
    if y2>(int(gridsize)-1):
        y2=int(gridsize)-1
    if y2<0:
        y2=0
    if y1>(int(gridsize)-1):
        y1=int(gridsize)-1
    return x1,y1,x2,y2

class led_grid:
    def  __init__(self,size):
        self.size= size
        self.grid=[[False]*size for _ in range(0,size)]
                
    def turn_on(self,x1,y1,x2,y2):
        
        for i in range(y1,y2+1):
            for j in range(x1,x2+1):
                self.grid[i][j]=True       
        return self.grid           
    
    def turn_off(self,x1,y1,x2,y2):
        for i in range(y1,y2+1):
            for j in range(x1,x2+1):
                self.grid[i][j]=False        
        return self.grid  
    
    def switch(self,x1,y1,x2,y2):
        for i in range(y1,y2+1):
            for j in range(x1,x2+1):
                if self.grid[i][j]==True:
                    self.grid[i][j]=False
                elif self.grid[i][j]==False:
                    self.grid[i][j]=True
        return self.grid
    
    def execute_instructions(self,command,x1,y1,x2,y2):
        if command=='turn on':
                self.turn_on(x1,y1,x2,y2)
        elif command=='turn off':
                self.turn_off(x1,y1,x2,y2)
        elif command=='switch':
                self.switch(x1,y1,x2,y2)
        return self.grid
        
    def count_leds(self):
        LEDS=0
        for i in range(0,self.size):
                for j in range(0,self.size):
                    if self.grid[i][j]==True:
                        LEDS+=1
        return LEDS
                    
def main():
    urlname=read_url()[2]
    if urlname.startswith('http://'):
        gridsize,content=read_url()[0],read_url()[1]
        c=led_grid(int(gridsize))
        for i in range(len(content)):
            command,x1,y1,x2,y2=content[i][0],int(content[i][1]),int(content[i][2]),int(content[i][3]),int(content[i][4])  
            cc=clean_up(gridsize, x1, y1, x2, y2)
            c.execute_instructions(command,cc[0],cc[1],cc[2],cc[3])  
        print(urlname,c.count_leds(),"\nRuntime %s seconds" % (time.time() - start_time))
    else:
        print("Please enter a valid url(http:// included)")
            
if __name__ == '__main__':
    main()
    