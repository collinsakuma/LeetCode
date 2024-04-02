class Solution:
    def countGoodTriplets(self, arr, a, b, c):
        good_triplets = 0 # count of triplets that meet all "good" requirments

        # create three nested loop too iterate over all possible triplet combinations
        for i in range(len(arr) - 2):
            for j in range((i + 1), len(arr) - 1):
                for k in range((j + 1, len(arr))):
                    # check triplet for conditions
                    true_a = abs(arr[i] - arr[j]) <= a
                    true_b = abs(arr[j] - arr[k]) <= b
                    true_c = abs(arr[i] - arr[k]) <= c

                    # if all condition are true increment good_triplets
                    if all((true_a,true_b,true_c)):
                        good_triplets += 1

        return good_triplets