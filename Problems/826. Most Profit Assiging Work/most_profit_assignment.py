class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        profits = 0
        curr_max = 0 
        j = 0

        # create a jobs matrix, with the difficulty and profit of each job in a array sorted by the difficulty
        jobs = sorted(zip(difficulty, profit))
        # sort the workers
        worker.sort()

        # loop through workers
        for i in worker:
            # while there are still jobs available and the worker can perform the job continue the loop
            while j < len(jobs) and i >= jobs[j][0]:
                # find the max profit of the jobs that the worker can perform
                curr_max = max(curr_max, jobs[j][1])
                j += 1
            # add the max profit job that the worker can perform to profits
            profits += curr_max

        return profits 