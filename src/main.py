'''
Created on 27 Feb 2017
@author: pigna
'''
import urllib.request
import argparse
import re
import time
import numpy as np
start_time = time.time()    #timing the program to see the performance

class led_grid:
    def  __init__(self,size):
        self.size= size
        self.grid=np.full((size,size),False,dtype=bool) #initialise numpy array
                
    def turn_on(self,x1,y1,x2,y2):
        self.grid[x1:x2 + 1, y1:y2 + 1] = True  #changes every value in the range to True, no need for checking     
        return self.grid           
    
    def turn_off(self,x1,y1,x2,y2):
        self.grid[x1:x2 + 1, y1:y2 + 1] = False  #same as above    
        return self.grid  
    
    def switch(self,x1,y1,x2,y2):
        self.grid[x1:x2 + 1, y1:y2 + 1] ^= True    #xor for the switch
        return self.grid
    
    def clean_up(self,x1,y1,x2,y2):   #function to correct the data, in case the input is smaller or bigger than the grid
        if x1<0:
            x1=0
        if x2<0:
            x2=0   
        if x2>(self.size-1):
            x2=self.size-1
        if x1>(self.size-1):
            x1=self.size-1    
        if y1<0:
            y1=0
        if y2>(self.size-1):
            y2=self.size-1
        if y2<0:
            y2=0
        if y1>(self.size-1):
            y1=self.size-1
        return x1,y1,x2,y2
    
    def execute_instructions(self,command,x1,y1,x2,y2):  #based on the command read, it executes the instruction
        if command=='turn on':
                self.turn_on(x1,y1,x2,y2)
        elif command=='turn off':
                self.turn_off(x1,y1,x2,y2)
        elif command=='switch':
                self.switch(x1,y1,x2,y2)
        return self.grid
        
    def count_leds(self):
        LEDS=np.count_nonzero(self.grid)  #handy numpy function to count everything that is not zero (False)
        return LEDS

def read_url():
    parser = argparse.ArgumentParser()                   #parse, gets the input from the command line
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()
    urlname = args.input
    uri= urlname                                        #goes to the address, and reads the file
    req = urllib.request.urlopen(uri)
    content = req.read().decode('utf-8').split("\n")    #divide line by line
    array_size = content[0]                             #first line is the grid size
    instructions=[]
    for i in range(1,len(content)-1):                   #use REGEX to get the instructions that are valid
        pattern=re.compile("\s*(turn on|turn off|switch)\s*,*\s*(-{0,1}\d+)\s*,*\s*(-{0,1}\d+)\s*through\s*(-{0,1}\d+)\s*,*\s*(-{0,1}\d+)") #eliminates all unnecessary whitespace
        if pattern.match(content[i]) != None:
            parsed_content=pattern.match(content[i]).groups()
            instructions.append(parsed_content)
    return urlname,int(array_size),instructions
               
def main():
    urlname=read_url()[0]
    if urlname.startswith('http://'):
        gridsize,content=read_url()[1],read_url()[2]
        c=led_grid(gridsize)       #creates the object
        for i in range(len(content)):
            command,x1,y1,x2,y2=content[i][0],int(content[i][1]),int(content[i][2]),int(content[i][3]),int(content[i][4])  
            c.execute_instructions(command,c.clean_up(x1, y1, x2, y2)[0],c.clean_up(x1, y1, x2, y2)[1],c.clean_up(x1, y1, x2, y2)[2],c.clean_up(x1, y1, x2, y2)[3])
        print(urlname,"on:",c.count_leds(),"\nRuntime %s seconds" % (time.time() - start_time))
    else:
        print("Please enter a valid url(http:// included)")
            
if __name__ == '__main__':
    main()
    