def text(text):
    d = {}
    for i in text.split(' '):
        d[i] = len(i)
    output = ''
    for i in sorted(d.items(), key=lambda item: item[1]):
        output += i[0] + ' '
    return 'Output: ' + output[:-1]

print(text(input('Input: ')))