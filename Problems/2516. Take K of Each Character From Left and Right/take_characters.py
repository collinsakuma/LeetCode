from collections import defaultdict

class Solution:
    def takeCharacters(self, s, k):
        count_a = s.count('a') - k
        count_b = s.count('b') - k
        count_c = s.count('c') - k

        # if any have less than 0 then there is less than k number of occurances return -1
        if any(i < 0 for i in [count_a, count_b, count_c]):
            return -1
        
        dict = defaultdict(int) # set default dict

        length = left = output = 0

        for right in s:
            dict[right] += 1
            length += 1

            while dict['a'] > count_a or dict['b'] > count_b or dict['c'] > count_c:
                dict[s[left]] -= 1
                length -= 1
                left += 1

            output = max(output, length)

        return len(s) - output