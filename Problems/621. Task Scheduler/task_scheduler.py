from collections import Counter

class Solution:
    def lesatInterval(self, tasks, n):
        frequency = Counter(tasks) # create a dict of all the tasks and how many times they are needed
        max_frequency = max(frequency.values()) # find the highest frequency of any given task to be done

        max_frequency_tasks = 0 # number of tasks that have the same max frequency

        # find max_frequency_tasks
        for i in frequency.values():
            if i == max_frequency:
                max_frequency_tasks += 1

        # find the amount of intervals needed between finishing the tasks that occur the most
        cooling_intervals = (max_frequency - 1) * (n + 1) + max_frequency_tasks

        return max(cooling_intervals, len(tasks))