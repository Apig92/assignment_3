'''
Created on 27 Feb 2017

@author: pigna
'''
import urllib.request

def read_url(url):
    uri= url
    req = urllib.request.urlopen(uri)
    buffer = req.read().decode('utf-8').split("\n")
    array_size = buffer[0]
    return array_size

class led_grid:
    def  __init__(self,size):
        self.size= size
        self.grid=[[False]*size for _ in range(0,size)]
                
    def turn_on(self,x1,y1,x2,y2):
        
        for i in range(y1,y2):
            for j in range(x1,x2):
                self.grid[i][j]=True
               
            print(self.grid[i])  
               
    
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
    read_url("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")
    print(read_url("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"))
    c=led_grid(int(read_url("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")))
    c.turn_on(1,0,2,2)
    c.switch(0,0,5,2)
        
        

if __name__ == '__main__':
    main()
    