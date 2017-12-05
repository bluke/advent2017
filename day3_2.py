#!/usr/bin/python3
from math import *

def ptab(tab):
    for line in tab:
        for point in line :
            print(point,end="\t",sep="")
        print()

def size(i):
    return ceil(sqrt(i)/2)

def fill(tab,l,c):
    res=0
    for i in range(l-1,l+2):
        for j in range(c-1,c+2):
            res+= tab[i][j]
    tab[l][c] = res

def walk(tab, entery):
    e = entery*2-1
    c = entery
    l = entery
    tab[l][c]=1
    c+=1
    while c!=e or l!=e:
        fill(tab,l,c)
        if tab[l][c] > 277678:
            return tab[l][c]
        if tab[l][c-1] != 0 and tab[l-1][c] == 0:
            l+=-1
        elif tab[l+1][c] != 0 and tab[l][c-1] == 0:
            c+=-1
        elif tab[l][c+1] != 0 and tab[l+1][c] == 0:
            l+=1
        else:
            c+=1


data = 500
taille = size(data)
if taille%2 == 0:
    taille += 1
tab = [[0 for col in range(taille)] for row in range(taille)]
access = int((taille-1)/2)
res = walk(tab,access)
ptab(tab)
print(res)
