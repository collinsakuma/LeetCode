class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        n = len(arr)
        # initalize array to hold the possible frations and their decimal value
        arr_fractions = []

        # loop through all possible combinations of indexes in the array and add them to the list of fractions
        for i in range(n):
            for j in range(i + 1, n):
                arr_fractions.append([arr[i]/arr[j], f'{arr[i]}/{arr[j]}'])

        # sort the list of fractions by the decimal place value 
        arr_fractions.sort(key = lambda x:x[0])

        # set the output value to the kth smallest fraction and split the fraction into a array
        output = (arr_fractions[k-1][1].split('/'))

        # convert output values into integers
        output[0], output[1] = int(output[0]), int(output[1])

        # return the output
        return output