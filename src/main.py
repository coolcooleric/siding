'''
Created on 2010-11-14

@author: ericwang
'''
from brd import Brd
from value import itDeep
from move import move
from rule import Rule
from helper import Helper

def movew(frm, to, brd): 
    brd.w = move(frm, to, brd.w)
    Rule.refresh(to, brd.w, brd.b, brd)
    return brd

def moveb(frm, to, brd):
    brd.b = move(frm, to, brd.b)
    Rule.refresh(to, brd.b, brd.w, brd)
    return brd

test = Brd(0xC200, 0x1B)
#test = Brd(0x220,0x8400)
#test = Brd(0x20A, 0x440)
#test = Brd(0x620,0x4004)
#test = Brd(0x8200, 0x4800)
#test = Brd(0x2A0, 0x108)
#test = Brd(0x8220, 0xA)
test.paintbrd()

'''
result = max(test, depth = 5)
moveb(brd = test, *result[0]);
test.paintbrd()
'''

while True:
    if Rule.gameOver(test):
        break
    else: 
        result = itDeep(test, depth = 7, type = "max")
        moveb(brd = test, *result); 
        print('-'*50)       
        test.paintbrd()
        
        if Rule.gameOver(test):
            break
        
        result = itDeep(test, depth = 7, type = "min")
        movew(brd = test, *result);
        print('-'*50)  
        test.paintbrd()        
