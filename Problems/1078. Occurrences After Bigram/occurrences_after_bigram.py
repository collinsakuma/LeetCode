class Solution:
    def findOcurrences(self, text, first, second):
        answer = [] # create an empty list that will have words appened to it
        text_arr = text.split(" ") # turn the string into a list of words

        for i in range(len(text_arr) - 2): 
            # len(text_arr) - 2. Minus 2 because we need to account for the 0 index and
            # you canot check the last two words because there needs to another word after to add.
            if text_arr[i] == first and text_arr[i + 1] == second:
                # if the word at i is equal to first and the word at index (i + 1) is also equal to second append the third word at (i + 2) to the answer list 
                answer.append(text_arr[i + 2])
        return answer