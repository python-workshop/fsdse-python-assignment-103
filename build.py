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
