'''
Created on 2010-11-13

@author: Administrator
'''
def move(frm, to, s):
    '''
        set frm --> 0, to --> 1
    '''
    return ~ frm & s | to

def unmove(frm, to, s):
    return ~ to & s | frm

