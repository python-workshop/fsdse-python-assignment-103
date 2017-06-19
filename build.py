import re

def compress(string):
    if string is None:
        return None

    pattern = re.compile(r'([A-Za-z])(\1*)')
    repetitions = re.findall(pattern, string)
    compressed = ''
    for tup in repetitions:
        repeats = len(tup[1])
        if repeats > 0:
            compressed += '{}{}'.format(tup[0], repeats+1)
        else:
            compressed += tup[0]

    if len(compressed) == len(string):
        return string
    else:
        return compressed
