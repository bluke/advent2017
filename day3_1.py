#!/usr/bin/python3
import math
"""


          R = 5         .<d=R*2
    ^ . . . . 4 . . . . 
  2 | . . . . 3 . . . . 
  R | . . | - 2 - - . . 
  + | . . | | 1 - | . . 
  1 | . . | | 0 | | . . .<d=R
    | . . | - - > | . . 
    | . . - - - - > . . i
    | . . . . . . . > . .
    v . . . . . . . . > .<d=2R-1
                      ^
                     mval


"""

def ring(num):
    root = math.ceil(math.sqrt(num))
    return math.ceil((root-1)/2)

def maxval(ring):
    return ((ring*2)+1)**2

def offset(rindex,ring):
    return abs((rindex%(2*ring))-ring)




if __name__ == "__main__":
    data = 277678
    R = ring(data)
    mval = maxval(R-1)
    local = data - mval
    off = offset(local,R)
    dist = R+off
    print(R)
    print(mval)
    print(local)
    print(off)
    print(dist)

