def compress(string1):
    if string1 is '':
        return ''
    if string1 is None:
        return None
    result = ''
    count = 1
    result += string1[0]
    for i in range(0,len(string1)-1):
        if string1[i] == string1[i+1]:
            count +=1
        elif count >1:
            result += str(count)+string1[i+1]
            count = 1
        elif count == 1:
            result += string1[i+1]
    if(count > 1):
        result += str(count)
    if len(string1) == len(result):
        return string1
    else:
        return result
