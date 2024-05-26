class Solution:
    def wordBreak(self, s: str, wordDict):
        def word_check(s, wordDict, start, cur, res):
            if start == len(s) and cur:
                res.append(' '.join(cur))

            for i in range(start, len(s)):
                word = s[start:i + 1]

                if word in wordDict:
                    cur.append(word)
                    word_check(s, wordDict, i + 1, cur, res)
                    cur.pop()

        res = []
        word_check(s, set(wordDict), 0, [], res)

        return res