class Solution:
    def permute(self, nums):
        def depth_first_search(path, used, res):
            if len(path) == len(nums):
                res.append(path[:])
                return 

            for i, letter in enumerate(nums):
                if used[i]: # skip letter if used[i] = True
                    continue
            
            path.append(letter) # add letter to path and mark it as used
            used[i] = True
            depth_first_search(path, used, res)
            path.pop() # remove letter from path and mark it as unused
            used[i] = False
        
        res = []
        depth_first_search([], [False] * len(nums), res)
        return res
