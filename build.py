import itertools

def compress(st):
    dic={}
    cnt=0
    if st == None:
        return None
    if st == '':
        return ''
    s_op=''
    keys=[]
    groups=[]
    for k,g in itertools.groupby(st):
        keys.append(k)
        groups.append(list(g))
    print keys
    print groups
    for e in groups:
        if len(e)>1:
            s_op = s_op + e[0] + str(len(e))
        else:
            s_op = s_op + e[0]
    if(len(st)>len(s_op)):
        return s_op
    else:
        return st

# compress('AABCCCDDDD')
# Output :
# ['A', 'B', 'C', 'D']
# [['A', 'A'], ['B'], ['C', 'C', 'C'], ['D', 'D', 'D', 'D']]
# 'A2BC3D4'
