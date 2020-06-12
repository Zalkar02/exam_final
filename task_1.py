def listed(text):
    char = text[-2:] if text[-2] == '-' else text[-1]
    step = int(char)
    index = 0 
    l = text[:-3].split(' ') if len(char) == 2 else text[:-2].split(' ')
    length = len(l)-1
    while index <= length:
        if step < 0:
            if index + step >= 0:
                l.insert(index + step, l.pop(index))
        else:
            if length - index + step  <= length:
                l.insert(length - index + step, l.pop(length - index))
        index += 1
    output = ''
    for i in l:
        output += i + ' '
    return 'Output: ' + output[:-1]
    

print(listed(input('Input: ')))