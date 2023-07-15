class Solution:

    # below is first solution I came up with. Solution works but runs too slow resulting in a "Time Limit Exceeded"
    def getSumAbsoluteDifferences(self, nums):
        answer = []

        for num in nums:
            sum = 0
            for i in range(len(nums)):
                sum += abs(num - nums[i]) # increment the sum by taking the absolute value of num - (each index)
            answer.append(sum)
        return answer
    
    def getSumAbsoluteDifferences(self, nums):
        n = len(nums)

        sumBelow, sumAbove = 0, sum(nums)
        answer = []

        for i, num in enumerate(nums):
            sumAbove -= num
            answer.append(sumAbove - (n - 1 - i) * num + i * num - sumBelow)
            sumBelow += num
        
        return answer