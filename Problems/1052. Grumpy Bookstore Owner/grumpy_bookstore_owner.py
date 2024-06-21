class Solution:
    def maxSatisfied(self, customers, grumpy, minutes):
        n = len(customers)
        # create a matrix for each minutes that has the number of 
        # customers in the store and weather or not the store owner
        # is grumpy during that minute
        in_store = [list(a) for a in zip(customers, grumpy)]

        # count of satisfied customers
        satisfied = 0

        # loop through range of minutes
        for i in range(n):
            # if the store owner is not grumpy at that minute
            if in_store[i][1] == 0:
                # add to the number of satisfied customers
                satisfied += in_store[i][0]
                # set the number of customers at that minute as 0 ( mark as accounted )
                in_store[i][0] = 0

        # most customers made satisfied if owner is made happy
        most_made_satisfied = 0
        # count of current satisfied customers in period of minutes
        curr_satisfied = 0

        # loop through in_store minutes tracking index of each minute
        for idx, customers_in_store in enumerate(in_store):
            # add to the current satisfied customers count
            curr_satisfied += customers_in_store[0]
            # if idx is passed the number of minutes that can be made happy
            # curr_satisfied needs to be reduced by minute leaving minutes window
            if idx >= minutes:
                # reduced curr satisfied count by the minute no longer in the window
                curr_satisfied -= in_store[idx - minutes][0]
            # check for a new most satisfied customers
            most_made_satisfied = max(most_made_satisfied, curr_satisfied)

        # return the max customers that can be satisfied
        return satisfied + most_made_satisfied