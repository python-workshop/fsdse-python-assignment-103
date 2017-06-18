def compress(str):
    if(str==None):
        return None
    if(len(str)==0 or len(str)==1 or len(str)==2):
        return str
    ans=""
    count=1
    i=0
    while i<len(str)-1:
        j=i+1
        while j!=len(str) and str[i]==str[j]:
            count+=1
            j+=1
        if count==1:
            ans=ans+str[i]
        else:
            ans=ans+"{}{}".format(str[i],count)
        i=i+count
        count=1
    if(str[len(str)-1]!=str[len(str)-2]):
        ans=ans+str[len(str)-1]
    if(len(ans)==len(str)):
        return str
    else:
        return ans
