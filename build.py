def compress(s):
    strCmp = ''
    count = 1
    #print s
    if s is not None and len(s)>0 :
        print s
        for i in range(0,len(s)-1):
            if s[i] == s[i+1]:
                count = count + 1
                #print s[i]
            else:
                if count == 1:
                    strCmp += s[i]
                else:
                    strCmp += s[i]+str(count)
                    count = 1
        strCmp = strCmp+s[i+1]+ (str(count) if count > 1 else '')
        return s if len(strCmp) >= len(s)  else strCmp
    return s

#print compress('AAABCCDDDDE')
#print compress('')
