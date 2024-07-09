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
    
    def averageWaitingTimeTwo(self, customers):
        previous_order_finish_time = total_time = 0

        for arrive, order_time in customers:
            # if the previous customers order is already completed by the 
            # arrival time of the next customer
            if arrive >= previous_order_finish_time:
                # incrase the total time by the order_time ( no additional wait time )
                total_time += order_time
                # set a new previous order finish time for
                # when the current customers order has been finished
                previous_order_finish_time = arrive + order_time

            else:
                # - if the previous customers order was not finished when the next
                #   customer arrived :
                # - add to the total time the amount of time the next customer waits
                #   while the cheif is finishing up the previous customers order
                # - then add the time that it takes to make the next order
                total_time += (previous_order_finish_time - arrive + order_time)
                # add the order to set a new previous_order_finish_time
                previous_order_finish_time += order_time
        
        return total_time / len(customers)