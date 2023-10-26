class Solution:
    def selfDividingNumbers(self, left, right):
        self_dividing = [] # list of self dividing numbers in range from left to right numbers
        for i in range(left, right + 1): # loop though range
            curr = str(i) # save the current number being iterated as a string
            if "0" in curr: # if 0 is in the number then it is not self dividing, skip that number
                None
            else: # if no 0 present in number check each number in curr
                for j in curr: # loop though curr
                    flag = True # set flag to True initially, if number in curr is not a valid self dividing number, change flag
                    if int(curr) % int(j) != 0: # if curr is not divisible by j break from the curent iteration and set flag to False
                        flag = False
                        break
                if flag: # after all numbers have been loooped though check if flag is True
                    self_dividing.append(int(curr)) # if true append curr to the list of self_dividing numbers
        
        return self_dividing