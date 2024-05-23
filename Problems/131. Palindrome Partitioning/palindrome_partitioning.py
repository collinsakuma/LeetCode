class Solution:
    def partition(self, s):
        palindromes = []

        # helper function to check if a string is a valid palindrome
        def is_palindrome(string):
            return string == string[::-1]

        # recursive depth first search function
        def dfs(i, curr):
            # if we are checking if the entire string s is a palindrome return immideatly
            if i == len(s):
                palindromes.append(curr)
                return
            # create the unique substrings to check
            for j in range(i, len(s)):
                sol = s[i:j + 1]
                # check if the substring is a palindrome
                if is_palindrome(sol):
                    # if it is check its next substring
                    dfs(j+1, curr + [sol])
            return
        # call the dfs function
        dfs(0, [])

        # return the list of valid palandromic sub arrays
        return palindromes