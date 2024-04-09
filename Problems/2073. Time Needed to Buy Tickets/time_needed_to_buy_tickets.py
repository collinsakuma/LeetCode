class Solution:
    def timeRequiredToBuy(self, tickets, k):
        answer = 0
        while tickets[k] != 0: # while the person at index k still has tickets to buy continue the loop
            for i in range(len(tickets)):
                # for each person (index) in the line to buy tickets loop through each one
                if tickets[i] > 0:
                    # if the person at tickets[i] still has tickets to buy buy a ticket and minus 1 from the total 
                    tickets[i] = tickets[i] - 1
                    answer += 1 # increment the total time to buy k's tickets by 1
                if tickets[k] == 0:
                    # when person at index k finishes buying their tickets exit the loop as they dont need to wait for the 
                    # people after them in line to buy their tickets to exit the loop. 
                    break
        return answer # return seconds it took for person k to buy their tickets. 
    
    def timeRequiredToBuyTwo(self, tickets, k):
        seconds = 0

        # loop while the target person still has tickets to buy
        while tickets[k] != 0:
            for index, ticket in enumerate(tickets):
                # if that persons doesnt need to buy any more tickets do nothing
                if ticket == 0:
                    None
                # if at the target purchaser and they are buying their last ticket, return the time plus 1 for purchasing the last ticket
                elif index == k and tickets[index] == 1:
                    return seconds + 1
                # person buys a ticket add a second to time elapsed
                else:
                    tickets[index] -= 1
                    seconds += 1
        return seconds
    
    def timeRequiredToBuyThree(self, tickets, k):
        time = 0

        for index, ticket in enumerate(tickets):
            # for all people infront of person k in the que
            # - if they have less tickets than person k to buy then they will have bought all of their tickets before person k does
            # - if they have more than or just as many tickets to buy as person k they they can only buy the same number of tickets as person k
            if index <= k:
                time += min(tickets[index], tickets[k])
            # for people after person k
            # - they can buy k - 1 tickets because once person k buys their last ticket this person will not beable to buy anymore
            # - if they are buying less than person k - 1 tickets they can purchase all of them
            else:
                time += min(tickets[index], tickets[k] - 1)
        return time