""" My wrong try
def compress(s1):
    if s1 is '':
        return ''
    if s1 is None:
        return None
    l1 = [(x,s1.count(x)) for x in s1]
    l2 = sorted(set(l1), key=l1.index)
    s2 = "".join(str(x[0])+str(x[1]) for x in l2)
    s3 = s2.replace("1","")

    if len(s3)==len(s1):
        return s1
    else:
        return s3
    #print s3
#compress('AABBCC')
"""
def compress(s1):
    if s1 is '':
        return ''
    if s1 is None:
        return None
    result = ''
    count = 1
    result += s1[0]
    for i in range(0,len(s1)-1):
        if s1[i] == s1[i+1]:
            count +=1
        elif count >1:
            result += str(count)+s1[i+1]
            count = 1
        elif count == 1:
            result += s1[i+1]
    if(count > 1):
        result += str(count)
    if len(s1) == len(result):
        return s1
    else:
        return result
