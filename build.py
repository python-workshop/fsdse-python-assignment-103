import itertools

def compress(string):
    dic={}
    cnt=0
    if string == None:
        return None
    if string == '':
        return ''
    em_str = ''
    keys=[]
    values=[]
    for k,v in itertools.groupby(string):
        keys.append(k)
        values.append(list(v))
    print keys
    print values
    for element in values:
        if len(element)>1:
            em_str = em_str + element[0] + str(len(element))
        else:
            em_str = em_str + element[0]

    if(len(string)>len(em_str)):
        return em_str
    else:
        return string
