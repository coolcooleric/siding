'''
Created on 2010-11-14

@author: ericwang
'''
from helper import Helper
class Rule(Helper):
    @staticmethod        
    def refresh(to, now, next, brd):
        tmp = now ^ next  
        next = Rule.capture(tmp, to, now, next, Rule.h_capture)
        next = Rule.capture(tmp, to, now, next, Rule.v_capture)                    
        if now == brd.b:
            brd.w = next
        else:
            brd.b = next
    
    @staticmethod          
    def capture(composite, to, now, next, type):
        for i in type:
            if to & i[0] != to:
                continue
            if composite & i[0] != i[0]:
                if composite & i[1] == i[1] and to & i[1] and ~ to & i[1] & now and ~ to & i[1] & next and i[3] & now:                     
                    return Rule.kill(i[1], next) 
                elif composite & i[2] == i[2] and to & i[2] and ~ to & i[2] & now and ~ to & i[2] & next and i[4] & now:
                    return Rule.kill(i[2], next)  
        return next
     
    @staticmethod        
    def kill(match, opp):
        t = opp & match
        return opp & ~t          
    
    @staticmethod 
    def gameOver(brd):
        return brd.b in Helper.p or brd.w in Helper.p or brd.b == 0 or brd.w == 0
