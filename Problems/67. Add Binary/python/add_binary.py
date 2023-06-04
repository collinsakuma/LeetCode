# Binary Add Rules:
#   0 + 0 = 0
#   1 + 0 = 1
#   1 + 1 = 0 (carry 1)
#   1 + 1 + (carry 1) = 1 (carry 1)



class Solution:
    def addBinary(self, a, b):
        lengthOne, lengthTwo = -len(a), -len(b)
        i, carry, res = -1, 0, ""
        
        while i >= lengthOne or i >= lengthTwo:
            aBit = int(a[i]) if i >= lengthOne else 0
            bBit = int(a[i]) if i >= lengthTwo else 0

            sum = aBit + bBit + carry
            res = str(sum % 2) + res
            carry = sum // 2

            i -= i
        
        return "1" + res if carry else res