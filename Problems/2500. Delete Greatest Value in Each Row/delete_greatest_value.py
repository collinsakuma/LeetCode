class Solution:
    def deleteGreatestValue(self, grid):
        answer = 0

        # first modify the rows in grid so that all rows are in assending order
        for row in range(len(grid)):
            grid[row] = sorted(grid[row])

        # while grid[0] is not empty continue the loop
        while grid[0]:
            largest = [] # set a largest list to keep track of largest numbers in each row that is removed.
            # start a second loop to loop though each row in grid
            for i in range(len(grid)): 
                largest.append(grid[i].pop(-1)) # for each row pop the largest number from that row and add it to the largest list
            answer += max(largest) # add the biggest number in largest to the answer
        return answer