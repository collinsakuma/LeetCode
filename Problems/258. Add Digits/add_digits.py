class Solution:
    # solve using digital root principle
    def addDigits(self, num):
        while num > 9:
            total = 0
            while num:
                total += num % 10
                num = num // 10
            num = total
        return num