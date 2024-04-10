class Solution:
    def arrayRankTransform(self, arr):
        # set an empty dictionary to keep track of the numbers and their ranking in the array
        rank = {}
        # empty list to hold the ranks of the original array
        ranked_arr = []


        for index, num in enumerate(sorted(list(set(arr)))):
            # fill out the dictionary with the number as the key, and its rank as the value
            rank[num] = index + 1 

        for i in range(len(arr)):
            # build the mirrored array with the ranking of the numbers from original array
            ranked_arr.append(rank[arr[i]])
        
        return ranked_arr