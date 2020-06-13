def sum_str(l):
    return sum(map(int, l))

def sum_int(num):
    output = 0
    while True:
        if num < 10:
            output += num
            break
        output += num % 10
        num //= 10
    return output

a = input("Input: ")
print('Output: ', sum_str(list(a)))
print('Output: ', sum_int(int(a)))