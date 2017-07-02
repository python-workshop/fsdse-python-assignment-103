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
