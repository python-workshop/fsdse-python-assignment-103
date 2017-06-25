def compress(s1):
    if s1 is None or len(s1) == 0:
        return s1
    result = ''
    prev_char = s1[0]
    count = 0
    for char in s1:
        if char == prev_char:
            count += 1
        else:
            result += prev_char + (str(count) if count > 1 else '')
            prev_char = char
            count = 1
    result += prev_char + (str(count) if count > 1 else '')
    return result if len(result) < len(s1) else s1
