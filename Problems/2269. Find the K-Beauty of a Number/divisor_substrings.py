class Solution:
    def divisorSubstrings(self, num, k):
        output = 0
        str_num = str(num) # set a version of num but as a string

        if len(str_num) == 1: # the number is less than 10 then it will always be divisionble by itself
            return 1

        for i in range(len(str_num) - k + 1): # loop though i in range of len(str_num) - k + 1
            # check two conditions:
            # 1. check if substring does not equal 0
            # 2. check if the modulo of num divided by the substring equals 0
            if int(str_num[i:i + k]) != 0 and num % int(str_num[i:i + k]) == 0:
                # if both conditions are meet than the substring is a divisor of num, increment output by 1
                output += 1
        return output