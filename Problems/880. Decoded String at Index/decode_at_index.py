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
    
    def decodeAtIndexTwo(self, s, k):
        decoded_length = 0 # length of decoded string

        for char in s:
            if char.isdigit(): # if character is a number update decoded_length
                decoded_length *= int(char)
            else:
                decoded_length += 1 # if character is a letter increment decoded_length
        
        # loop through input string in reverse order to find the kth character
        for i in range(len(s) - 1, -1, -1):
            current_char = s[i]

            if current_char.isdigit():
                # if character is a number adjust decoded_length and k
                decoded_length //= int(current_char)
                k %= decoded_length
            else:
                # if character is a letter check if it is the kth character
                if k == 0 or decoded_length == k:
                    return current_char
                decoded_length -= 1
        return ""