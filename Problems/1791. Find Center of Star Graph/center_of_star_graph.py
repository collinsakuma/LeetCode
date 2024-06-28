class Solution:
    def findCenter(self, edges):
        dict = {}

        # loop through edges
        for left, right in edges:
            # - if the points arnt in the dictionary create a new entry
            # - if the points are in the dictionary increment their value
            # - if the count of the edge value is equal to the length of edges list
            #    return the value as the center has been found
            if left not in dict:
                dict[left] = 1
            else:
                dict[left] += 1
                if dict[left] == len(edges):
                    return left
            if right not in dict:
                dict[right] = 1
            else:
                dict[right] += 1
                if dict[right] == len(edges):
                    return right