import re

def compress(og_string):
    string = og_string
    if string is not None:
        while(re.search(r'([a-zA-z])\1{1,}', string)):
            temp = re.search(r'([a-zA-z])\1{1,}', string).group(0)
            string = re.sub(temp, temp[0]+str(len(temp)), string)
        return string if len(string) < len(og_string) else og_string
    else:
        return og_string

#def compress_string(string):
#    if string is not None or len(string)> 0:
#        result = ''
#        prev_char = string[0]
#        count = 0
#        for char in string:
#            if char == prev_char:
#                count += 1
#            else:
#                result += prev_char + (str(count) if count > 1 else '')
#                prev_char = char
#                count = 1
#        result += prev_char + (str(count) if count > 1 else '')
#        return result if len(result) < len(string) else string

output=compress('AAABCCDDDD')
print output
