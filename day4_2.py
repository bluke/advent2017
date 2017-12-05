#!/usr/bin/python

def get(filename):
    res = []
    with open(filename) as fd :
        for line in fd :
            res.append(line.rstrip().split())
    return res

def validate(array):
    res = 0
    print(len(array))
    for line in array:
        for i in range(len(line)):
            line[i]=''.join(sorted(line[i]))
        line.sort()
        ok=True
        i=1
        while i<len(line) and ok:
            if line[i]==line[i-1]:
                res+=1
                ok=False
            i+=1
    print(res)
    return len(array)-res


data = get("day4.in")
print(validate(data))
