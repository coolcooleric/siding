'''
Created on 2010-11-14

@author: Administrator
'''
from Helper import Helper
from Move import move
from Brd import Brd
from Rule import Rule

def calc(brd):
    if brd.b in Helper.p or brd.b == 0:
        return -64
    if brd.w in Helper.p or brd.w == 0:
        return 64
    sum = 0
    for i in Helper.p:
        if brd.b & i:
            sum += 3
            if i == Helper.p[5] or i == Helper.p[6]\
               or i == Helper.p[9] or i == Helper.p[10]:
                sum += 1
        elif brd.w & i:
            sum -= 3
            if i == Helper.p[5] or i == Helper.p[6]\
               or i == Helper.p[9] or i == Helper.p[10]:
                sum -= 1
    return sum

def itDeep(brd, depth, type):
    if depth == 0:
        return ((),calc(brd))
    i = 1
    best = ()
    while i <= depth:
        if type == 'max':
            result = max(brd, depth = i, bb = 64, best = best)
            if result[1] == 64:
                return result[0]
        else:
            result = min(brd, depth = i, aa = -64, best = best)
            if result[1] == -64:
                return result[0]
        best = result[0]
        i += 1
    return best

#    if type == 'max':
#        return max(brd, 64, depth, ())[0]
#    else:
#        return min(brd, -64, depth, ())[0]

def max(brd, bb=64, depth=10, best=()):
    if depth == 0:
        return ((), calc(brd))  
    bestmove = () 
    val = -64  
    moves = brd.getMove(brd.b)
    if len(moves) == 0:
       return (bestmove, -64) 
    if len(best) > 0:
        moves.append(best)
    for i in range(len(moves)-1, -1, -1):
        if best and i < len(moves)-1 and moves[i] == best:
            continue;
        b = move(moves[i][0], moves[i][1], brd.b)
        tmp = Brd(b, brd.w)
        Rule.refresh(moves[i][1], tmp.b, tmp.w, tmp)
        response = min(tmp, val, depth - 1, best=())[1]
        if response > bb:
            bestmove = moves[i]
            val = response
            break;
        if response > val:
            bestmove = moves[i]
            val = response
    if val == -64: #black lose anyway
        bestmove = moves[0]
    return (bestmove, val)
 
def min(brd, aa= -64, depth=10, best=()):
    if depth == 0:
        return ((), calc(brd))
    val = 64
    bestmove = ()
    moves = brd.getMove(brd.w)
    if len(moves) == 0:
       return (bestmove, 64) 
    if best:
        moves.append(best)
    for i in range(len(moves)-1, -1, -1):
        if best and i < len(moves)-1 and moves[i] == best:
            continue;
        w = move(moves[i][0], moves[i][1], brd.w)
        tmp = Brd(brd.b, w)
        Rule.refresh(moves[i][1], tmp.w, tmp.b, tmp)
        response = max(tmp, val, depth - 1, best=())[1]
        if response < aa:
            bestmove = moves[i]
            val = response
            break
        if response < val:
            bestmove = moves[i]
            val = response
    if val == 64: #white lose anyway
        bestmove = moves[0]
    return (bestmove, val)     

