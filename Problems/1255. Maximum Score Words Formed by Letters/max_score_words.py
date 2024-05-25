class Solution:
    def maxScoreWords(self, words, letters, score):
        def choose_max(n, letter):
            if n == len(words):
                return 0
            
            output = 0
            copy = letter

            for i in words[n]:
                if i not in copy:
                    return choose_max(n + 1, letter)
                copy = copy.replace(i, '', 1)
                output += score[ord(i)-97]
            
            return max(choose_max(n + 1, letter), output + choose_max(n + 1, copy))

        return choose_max(0, ''.join(letters))