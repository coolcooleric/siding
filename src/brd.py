'''
Created on 2010-11-8

@author: ericwang
'''
from helper import Helper
class Brd(Helper):  
        
    def __init__(self, b, w):
        self.b = b
        self.w = w
        
    def paintbrd(self):
        ''' paint the board
        '''
        brd = []
        hs = '-' * 3
        vs = '|'  
        for i in self.p:
            if self.b & i:
                brd.append('B')
            elif self.w & i:
                brd.append('W')
            else:
                brd.append(' ')            
            if 1 << 12 == i or 1 << 8 == i or 1 << 4 == i:
                brd.append('\n')
                brd.append((vs + ' ' * 3) * 3 + vs)
                brd.append('\n')
            elif 1 == i:
                pass
            else:
                brd.append(hs)
        print(''.join(brd))
         
    def getMove(self, b):
        moves = []
        for i in self.p:
            if b & i:                
                    for m in self.dir_mapping.keys():
                        if i & self.dir_mapping[m][0]:
                            continue
                        tmp = self.dir_mapping[m][1](i)
                        if tmp & self.b or tmp & self.w:
                            pass
                        else:
                            moves.append((i,tmp))          
        return moves 

         
                 
     

'''    
brd = Brd(0x40,0xF)
brd.paintbrd()


for move in brd.getMove(brd.b):
    print('{0}:{1}'.format(hex(move[0]), hex(move[1])))

from Move import move
from Move import unmove
t = brd.getMove(brd.b)[0]
brd.b = move(s = brd.b,*t)
brd.paintbrd()
brd.b = unmove(s = brd.b,*t)
brd.paintbrd()
'''
   
if __name__ == 'main':
    pass

