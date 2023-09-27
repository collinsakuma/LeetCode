class Solution:
    # first attempt Memory Limit Exceeded error encountered for test with large s and k
    def decodeAtIndex(self, s, k):
        tape = ""
        # loop through each element in string s
        for i in s:
            # if tape is longer than the index that is being searched for exit the loop
            if len(tape) > k:
                break
            # check if i is a number, if so multiply the current tape by i  - 1
            #   - minus count by 1 because the tape already consist of one instance of the sequence being mutiplied
            if i.isdigit():
                tape += tape * (int(i) - 1)
            # if i is a letter add the letter to the tape
            else:
                tape += i
        return tape[k - 1] # return the kth letter in the tape, - 1 to account for 0 index