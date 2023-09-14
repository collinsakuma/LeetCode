class Solution:

    # first solution that I came up with TLE 

    def removeStars(self, s):
        s = list(s) # turn string s into a list
        while "*" in s: # while there are * in the list s countinue to loop
            index = s.index("*") # set an index for a found *
            left = index - 1 # variable to the left of the *
            while s[left] == "*": # if left is a * increment left by -1
                left = left - 1
            # remove the * and remove the first letter left of index
            s.pop(index)
            s.pop(left)
        return "".join(s) # return the list returned into a string
    

    def removeStarsTwo(self, s):
        output = [] # empty list to add letters too

        for i in s: # loop though each letter in s
            # if i is *, pop() the last index in output
            if i == "*":
                output.pop()
            else: # else add the letter to output
                output.append(i)
        return "".join(output) # return the list joined as a string