from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula):
        counts = defaultdict(int)
        stack = []
        multiplier = 1
        num = ''
        element = ''

        for i in range(len(formula) - 1, -1, -1):
            c = formula[i]
            if c.isdigit():
                num = c + num
            elif c.isalpha():
                element = c + element
                if c.isupper():
                    counts[element] += multiplier * (int(num) if num else 1)
                    element, num = '', ''
            elif c == ')':
                multiplier *= int(num) if num else 1
                stack.append(int(num) if num else 1)
                num = ''
            else:
                multiplier //= stack.pop()
        
        result = []
        for key in sorted(counts.keys()):
            result.append(key)
            if counts[key] > 1:
                result.append(str(counts[key]))
        return ''.join(result)