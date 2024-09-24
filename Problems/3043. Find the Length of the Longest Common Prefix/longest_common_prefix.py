class Solution:
    def longestCommonPrefix(self, arr1, arr2):
        st = set()

        # build a prefix set for the first array
        for num in arr1:
            # convert the num to string
            str_num = str(num)
            # initalize the prefix
            prefix = ""
            
            # loop through the numbers in num
            for ch in str_num:
                # build the prefix
                prefix += ch
                # add each prefix to the set of arr1 prefixes
                st.add(prefix)

        # set max_length of common prefix to 0
        max_length = 0

        # loop through nums in arr2
        for num in arr2:
            # convert the num to a string
            str_num = str(num)
            # initalize a prefix
            prefix = ""

            # loop through each num in num
            for ch in str_num:
                # build the prefix
                prefix += ch
                # check if the prefix is in the arr1 prefix set
                if prefix in st:
                    # if the prefix is in the set check for a new longest prefix
                    max_length = max(max_length, len(prefix))

        return max_length # retunr the length of the longest common prefix