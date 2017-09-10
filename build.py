def compress(x):
	if x is None or len(x) == 0:
		return x
	result = ''
	last_char = x[0]
	count = 0
	for i in x:
		if i == last_char:
			count += 1
		else:
			result += last_char + (str(count) if count > 1 else '')
			last_char = i
			count = 1
	result += last_char + (str(count) if count > 1 else '')
	return result if len(result) < len(x) else x
