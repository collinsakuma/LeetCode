class Solution:
    def minAddToMakeValid(self, s):
        # count open and closed parentheses without pair
        open_p, closed_p = 0, 0

        # loop through parentheses
        for i in s:
            # if an opening parentheses incrase count of open parentheses
            if i == '(':
                open_p += 1
            # if a closed parentheses
            else:
                # if there are currently no open parentheses to close
                # incresae the count of closed parentheses
                if not open_p:
                    closed_p += 1
                # if there are open parentheses that can be closed close one out
                else:
                    # on pair has been made reduce count of open parentheses without pair
                    open_p -= 1

        # return the number of open and colosed parentheses that need to be closed out
        return open_p + closed_p