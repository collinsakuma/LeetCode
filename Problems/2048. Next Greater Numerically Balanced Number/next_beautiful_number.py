from collections import Counter

class Solution:
    def nextBeautifulNumber(self, n):
        # set flag for when a beautiful number is found to True initially
        is_beautiful = True

        # while a beautiful number has not been found continue the loop
        while is_beautiful:
            # increment n
            n += 1
            # create a counter for n
            counter = Counter(str(n))
            # set flag to initial False
            flag = False
            # loop through items in counter
            for num, count in counter.items():
                # if the number value and the count of the number do not
                # match flip the flag and break from the loop
                if int(num) != count:
                    flag = True
                    break
                # if the flag remains False after the loop has executed then
                # a beautiful number has been found
                if not flag:
                    # flip the beautiful flag
                    is_beautiful = False

        return n # return the beautiful number
