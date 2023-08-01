class Solution:
    def digitSum(self, s, k):
        while len(s) > k: # while the length of s is greater than k loop will continue to run
            num_set = [s[i:i+k] for i in range(0, len(s), k)] # create a list of strings that are of k length

            s = "" # set s to an emtpy string
            for j in num_set: # loop though the strings in num_set
                val = 0
                for n in j: # loop though each string of k length in num_set
                    val += int(n) # sum each n into the val variable
                s += str(val) # add the sum of each n to the s string
        return s