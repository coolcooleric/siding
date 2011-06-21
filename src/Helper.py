'''
Created on 2010-11-14

@author: Administrator
'''

class Helper:
    '''
    classdocs
    '''
    p = (0x8000, 0x4000, 0x2000, 0x1000,
     0x800, 0x400, 0x200, 0x100,
     0x80, 0x40, 0x20, 0x10,
     0x8, 0x4, 0x2, 0x1)    
    
    h_capture = ((0xF000, 0x7000, 0xE000, 0x2000, 0x4000),
                 (0xF00, 0x700, 0xE00, 0x200, 0x400),
                 (0xF0, 0x70, 0xE0, 0x20, 0x40),
                 (0xF, 0x7, 0xE, 0x2, 0x4))
    v_capture = ((0x8888, 0x8880, 0x888, 0x800, 0x80),
                 (0x4444, 0x4440, 0x444, 0x400, 0x40),
                 (0x2222, 0x2220, 0x222, 0x200, 0x20),
                 (0x1111, 0x1110, 0x111, 0x100, 0x10))
    
    dir_mapping = {'left':(0x8888,lambda i:  i << 1),
                   'right':(0x1111,lambda i: i >> 1),
                   'up':(0xF000,lambda i: i << 4),
                   'down':(0xF,lambda i: i >> 4)}
        