class Solution:
    def getLucky(self, s, k):
        new_s = ""

        for letter in s:
            new_s += str(ord(letter) - 96)
        while k != 0:
            transform = 0
            for num in str(new_s):
                transform += int(num)
            new_s = transform
            k -= 1
        return new_s
    