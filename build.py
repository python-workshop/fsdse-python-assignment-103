def compress(input_str):
    if input_str is None:
        return

    final_str = ''
    input_str_list = list(input_str)
    count = 1
    for index, ch in enumerate(input_str_list):
        if index > 0:
            if ch == input_str_list[index-1]:
                count += 1
                if count > 2:
                    p = list(final_str)
                    p[-1] = str(count)
                    new_str = ''.join(p)
                    final_str = new_str
                else:
                    final_str += str(count)
            else:
                final_str += ch
                count = 1
        else:
            final_str += ch

    return final_str
