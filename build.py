import itertools
def compress(string):
    if string is None:
        return None
    data = []
    for i in string:
        data.append(i)
    groups = []
    uniquekeys = []
    for k, g in itertools.groupby(data):
        groups.append(list(g))
        uniquekeys.append(k)

    resultlist = []
    for i,j in zip(groups, uniquekeys):
        if len(i) != 1:
            resultlist.append(j+str(len(i)))
        else:
            resultlist.append(j)
    if len(resultlist)*2 == len(string):
        return string
    else:
        return "".join(resultlist)
