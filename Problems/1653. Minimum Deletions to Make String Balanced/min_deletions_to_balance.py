class Solution:
    def minimumDeletions(self, s):
        n = len(s)
        # create two lists to track the amount of b's before index and a's after index
        count_a = count_b = [0] * n
        # keep a running count of 'a' and 'b' that have been iterated over
        num_a = num_b = 0

        # loop through range of n skipping over the first ( 0 ) index
        for i in range(1, n):
            # if there is a leading b increase its count
            if s[i - 1] == 'b':
                num_b += 1
            # set index i to the number of leading b's that index has
            count_b[i] = num_b

        # loop through range of n in reverse order
        for i in range(n - 2, -1, -1):
            # if there is a trailing a increase the count of a's
            if s[i + 1] == 'a':
                num_a += 1
            # set the count of a's that occur after index i
            count_a[i] = num_a

        # find the index with the minimum sum after removing the leading b's before that index and
        # the trailing a's after that index
        min_cost = [sum(i) for i in zip(count_a, count_b)]

        return min(min_cost)