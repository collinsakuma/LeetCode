class Solution:
    def averageWaitingTime(self, customers):
        wait = [] # set an empty array to keep track of wait time per customer
        time = 0 # set a starting time at 0 because the chef has not yet recived any orders

        for i, j in customers: # loop though each customer array in customers
            if (i > time): # if the time the customer puts in their order is greater than the current time 
                time = i + j # set time equal to the time the customer puts in their order plus how much time the order takes to complete
            else: # else if i is less than the current time, meaning the chef is working on someone elses order
                time += j # increase time by the time it take to make the next persons meal, essentailly queing them 
            wait.append(time - i) # append the total wait time for each customer to the wait list
        return sum(wait) / len(wait) # return the average wait time sum and divide by the number of customers