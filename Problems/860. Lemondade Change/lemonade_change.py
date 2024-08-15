class Solution:
    def lemonadeChange(self, bills):
        # dict to hold the bills that we recieve
        change = {20: 0, 10: 0, 5: 0}

        # loop through the bills
        for bill in bills:
            # add the bill to the change dict
            change[bill] += 1
            # calculate the change that is due to the cusotmer
            change_due = bill - 5

            # loop while we still owe change
            while change_due:
                # if the change due is more than $10 and we have $10 bills available
                if change_due >= 10 and change[10] > 0:
                    # give the customer a $10 as change, reduce our count of $10 bills
                    # and reduce the change due by $10
                    change[10] -= 1
                    change_due -= 10
                # if the change due is $5 or more and we have $5 bills 
                elif change_due >= 5 and change[5] > 0:
                    # give the customer a $5 bill as change reduce both count of $5 bills
                    # and change due by 5
                    change[5] -= 1
                    change_due -= 5
                # if we dont have the correct change to give the customer return False
                else:
                    return False
        
        return True
