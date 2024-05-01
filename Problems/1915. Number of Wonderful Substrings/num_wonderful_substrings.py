from collections import defaultdict

class Solution:
    def wonderfulSubstrings(self, word):
        output, mask = 0, 0

        frequency = defaultdict(int, {0:1})

        for char in word:
            mask ^= 1 << ord(char) - 97
            output += frequency[mask]

            for i in range(10):
                output += frequency[mask ^ 1 << i]

            frequency[mask] += 1

        return output