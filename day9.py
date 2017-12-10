

def rec_crawler(strng, lvl):
    grp = 0
    grb = 0
    if strng[0] == "{":
        pts = lvl+1
    elif strng[0] == "<":
        pts = 0
    else:
        print("Error : worgn start", strng, lvl)

    wrk = strng[1:]
    cont = True

    while cont:
        char = wrk[0]
        if pts == 0:
            if char == '!':
                wrk = wrk[1:]
            elif char == '>':
                cont = False
            else:
                grb += 1
        else:
            if char == '<':
                wrk, _, sgrb = rec_crawler(wrk, pts)
                grb += sgrb
                continue
            elif char == '{':
                wrk, sgrp, sgrb = rec_crawler(wrk, pts)
                grp += sgrp
                grb += sgrb
                continue
            elif char == '}':
                cont = False
            else:
                pass
        wrk = wrk[1:]
    return (wrk, pts+grp, grb)



with open("day9.in") as fd:
    strm = fd.readline().rstrip()

res, tot, grb = rec_crawler(strm, 0)
print(res, tot, grb)
