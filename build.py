def compress(string):
    if string is None or len(string) == 0:
        return string
    result = ''
    prev_char = string[0]
    count = 0
    for char in string:
        if char == prev_char:
            count += 1
        else:
            result += prev_char + (str(count) if count > 1 else '')
            prev_char = char
            count = 1
    result += prev_char + (str(count) if count > 1 else '')
    return result if len(result) < len(string) else string
