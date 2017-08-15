def compress(s):
    if s is None or s == '':
        return s
    char = s[0]
    count = 0
    c_str = ''
    for c in s:
        if c == char:
            count += 1
        else:
            if count != 1:
                c_str += char + str(count)
            else:
                c_str += char
            char = c
            count = 1
    if count != 1:
        c_str += char + str(count)
    else:
        c_str += char
    return c_str if len(c_str) < len(s) else s
