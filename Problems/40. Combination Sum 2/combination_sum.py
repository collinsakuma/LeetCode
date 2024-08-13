class Solution:
    def combinationSum2(self, candidates, target):
        output = []
        # sort the list of numbers in ascending order
        candidates.sort()

        # depth first search
        def dfs(index, path, curr):
            # if curr sum is greater than the target return as target threshold has been passed
            if curr > target:
                return 
            # if the target has been reached append the list to the list of combinations
            if curr == target:
                output.append(path)
            
            # loop through range from index variable to length of candidates list
            for i in range(index, len(candidates)):
                # if current index in loop is greater than index variable check if curent value is equal to the previous
                if i > index and candidates[i] == candidates[i - 1]:
                    # if they are equal skip the value ( avoid dupilcate combinations )
                    continue
                # traverse to next in candiates by feeding it back into the dfs
                dfs(i + 1, path + [candidates[i]], curr + candidates[i])
        
        dfs(0, [], 0)

        return output