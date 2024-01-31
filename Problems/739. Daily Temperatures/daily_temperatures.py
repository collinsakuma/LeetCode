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
    

    # solution created on 1/31/24 will work on shorter test cases but TLE on longer ones. 
    def dailyTemperaturesTwo(self, temperatures):
        output = []

        for i in range(len(temperatures)):
            flag = False

            for j in range(i, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    output.append(j - i)
                    flag = True
                    break
                if not flag:
                    output.append(0)

        return output