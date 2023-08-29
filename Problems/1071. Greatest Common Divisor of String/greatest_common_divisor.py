import math

class Solution:
    def gcdOfString(self, str1, str2):
        if str1 + str2 != str2 + str1:
            # if a combined string of str1 + str2 and str2 + str1 are the same that means they share a common prefix 
            # for exaple:
            # if str1 = "ABCABC" str2 = "ABC"
            # str1 + str2 = "ABCABCABC" and str2 + str1 = "ABCABCABC" both outputs are equal
            # if str1 = "LEET" and str2 = "CODE"
            # str1 + str2 = "LEETCODE" and str2 + str1 = "CODELEET" the two outputs are not equal nor do they share a prefix
            return ""

        return str1[:math.gcd(len(str1), len(str2))]
        # math.gcd will return the greatest common denominator for 2 inputs
        # str1[:greatestCommonDenominator] will return the largest prefix that both strings share