#!/usr/bin/python3
from copy import deepcopy as cp

init = [4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3]

bank = []

def redistribute(tab):
    size = max(tab)
    strt = tab.index(size)
    tab[strt]=0
    strt
    while size > 0:
        strt = (strt+1)%len(tab)
        tab[strt] += 1
        size -= 1

def check(tab,bank):
    res = False
    i = 0
    while i < len(bank) and not res:
        if tab == bank[i]:
            res = True
        i+=1
    return res


bank.append(cp(init))
runs=1
redistribute(init)
while not check(init,bank):
    bank.append(cp(init))
    runs+=1
    redistribute(init)
print(runs)
print(len(bank)-bank.index(init))
