class Solution:
    def dailyTemperatures(self, temperatures):
        output = [0] * len(temperatures)
        stack = []

        for i, j in enumerate(temperatures):
            # check if current value is greater than last appened stack value
            while stack and stack[-1][1] < j:
                index, value = stack.pop()
                output[index] = i - index # check how many indicies have been crossed since last lesser temperature
            stack.append([i, j])
        return output 