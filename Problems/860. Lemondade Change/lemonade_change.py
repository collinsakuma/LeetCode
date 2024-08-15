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
    
    def lemonadeChangetwo(self, bills):
        # only keep track of $5 and $10 bills as $20 bills cannot be used as change 
        count_5, count_10 = 0, 0

        # loop through bills
        for bill in bills:
            # if bill is a $5 increment count_5
            if bill == 5:
                count_5 += 1
            # if bill is a $10 increment count_10
            elif bill == 10:
                count_10 += 1
                # check if we have any $5 for change
                if not count_5:
                    # if there are no $5 for change return False
                    return False
                # decrement count of $5's
                count_5 -= 1
            # last case is if the bill is a $20
            else:
                # if there are $5's and $10's available
                if count_5 and count_10:
                    # use one of each for the change
                    count_10 -= 1
                    count_5 -= 1
                # if there are no $10's but we have at least 3 $5's
                # give the change back in $5's, reduce count accordinly
                elif count_5 > 2:
                    count_5 -= 1
                else:
                    # we dont have the necessary bills to give change return False
                    return False
            # all bill are completed with correct change return True
        return True