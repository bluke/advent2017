
data=[]

with open("day8.in") as fd:
    for line in fd:
        data.append(line.split())

reg = {}
maxval = 0

for ins in data:
    treg = reg.setdefault(ins[0], 0)
    creg = reg.setdefault(ins[4], 0)
    cval = int(ins[6])
    if ins[1] == "inc":
        dlt = int(ins[2])
    elif ins[1] == "dec":
        dlt = -1*int(ins[2])
    else:
        print("ERROR :", ins)

    if ins[5] == "==":
        if creg == cval:
            reg[ins[0]] = treg+dlt
    elif ins[5] == "!=":
        if creg != cval:
            reg[ins[0]] = treg+dlt
    elif ins[5] == "<":
        if creg < cval:
            reg[ins[0]] = treg+dlt
    elif ins[5] == "<=":
        if creg <= cval:
            reg[ins[0]] = treg+dlt
    elif ins[5] == ">":
        if creg > cval:
            reg[ins[0]] = treg+dlt
    elif ins[5] == ">=":
        if creg >= cval:
            reg[ins[0]] = treg+dlt
    else:
        print("ERROR :", ins)

    if reg[ins[0]] > maxval:
        maxval = reg[ins[0]]

print(max(reg.values()))
print(maxval)
