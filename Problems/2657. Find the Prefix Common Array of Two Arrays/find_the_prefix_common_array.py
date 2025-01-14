class Solution:
    def findThePrefixCommonArray(self, A, B):
        n = len(A)
        # list to hold unpaired numbers from A and B arrays
        new_a, new_b = [], []
        # list to hold count of common prefixes
        common_prefix_array = [0] * n
        
        # loop through the range of the array length
        for i in range(n):
            # accumulate the count of all previous indexes
            if i != 0:
                common_prefix_array[i] += common_prefix_array[i - 1]

            # if index i is the same in each array they are a common prefix add 1 to count
            if A[i] == B[i]:
                common_prefix_array[i] += 1
            # if A[i] and B[i] are in eachothers array
            # add nothing and remove their complement
            elif A[i] in new_b and B[i] in new_a:
                new_b.remove(A[i])
                new_a.remove(B[i])
                # increment common prefix array by 2 as 2 prefixes have been found
                common_prefix_array[i] += 2
            # if A[i] is in B but B[i] is not in A
            # - remove A[i] from B 
            # - add B[i] to B
            elif A[i] in new_b and B[i] not in new_a:
                new_b.remove(A[i])
                new_b.append(B[i])
                # increment common prefix by 1 
                common_prefix_array[i] += 1
            # if B[i] in A but A[i] not in B
            elif B[i] in new_a and A[i] not in new_b:
                new_a.remove(B[i])
                new_a.append(A[i])
                common_prefix_array[i] += 1
            # A[i] and B[i] are not prefixes of eachother
            # add both to their array
            else:
                new_a.append(A[i])
                new_b.append(B[i])

        return common_prefix_array # return count of common prefixes at each index