def addToArrayForm(num, k): # solution works. It runs too slow
    num_string = ""
    for i in num:
        num_string += str(i)
    num_string = int(num_string) + k
    return [int(i) for i in str(num_string)]


# divmod(divided, divisor)
# divided - The number you want to divide
# divisor - The number you want to divide with
def addToArrayFormTwo(self, num, k):
    for i in range(len(num) - 1, -1, -1):
        k, num[i] = divmod(num[i] + k, 10)
    while k:
        k, a = divmod(k, 10)
        num = [a] + num
    return num