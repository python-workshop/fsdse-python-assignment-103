def compress(s):
    if s is None or len(s) == 0:
        return s
    result = ''
    prev_char = s[0]
    count = 0
    for char in s:
        if char == prev_char:
            count += 1
        else:
            result += prev_char + (str(count) if count > 1 else '')
            prev_char = char
            count = 1
    result += prev_char + (str(count) if count > 1 else '')
    return result if len(result) < len(s) else s
compress('AABBBCDDEEEE')
