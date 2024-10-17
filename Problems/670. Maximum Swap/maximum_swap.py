class Solution:
    def maximumSwap(self, num):
        str_num = str(num) # convert the number to a string
        greatest_num = num # save the num as the current greatest number found

        # initial loop to point at the number that we are looking to swap
        for i in range(len(str_num)):
            # initalize a second loop to search for number to the right of i that is larger to swap
            for j in range(i + 1, len(str_num)):
                # if a larger number is found
                if str_num[i] < str_num[j]:
                    # create a new number and swap the two indexes
                    possible_num = list(str_num)
                    possible_num[i], possible_num[j] = str_num[j], str_num[i]
                    # check for a new greatest number
                    greatest_num = max(greatest_num, int(''.join(possible_num)))

        return greatest_num # return the greatest number found