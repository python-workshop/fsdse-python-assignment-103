def compress(user_string):

    op_string = ""
    count = 1

    if user_string == None:
        return None
    elif user_string == '':
        return ''

    op_string += user_string[0]
    for i in range(len(user_string)-1):
        if(user_string[i] == user_string[i+1]):
            count+=1
        else:
            if(count > 1):
                op_string += str(count)
            op_string += user_string[i+1]
            count = 1
    if(count > 1):
        op_string += str(count)

    if len(op_string) == len(user_string):
        return user_string
        
    return op_string

user_string = "AAABCCDDD"
compress(user_string)
