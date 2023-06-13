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