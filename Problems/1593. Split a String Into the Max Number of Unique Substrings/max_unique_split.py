class Solution:
    def maxUniqueSplit(self, s):
        def backtrack(start, seen):
            # if the whole string has been looped without finding a max_split return 0
            if start == len(s):
                return 0
            
            max_split = 0

            # try all substrings starting from index start
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if substring not in seen:
                    seen.add(substring) # if the substring is not in the set of substrings add it
                    # recursively check the next part of the substring
                    max_split = max(max_split, 1 + backtrack)
                    seen.remove(substring) # backtrack: remove the substring after exploring the path

            return max_split
        
        return backtrack(0, set())