class Solution:
    def buildArray(self, target, n):
        output = []

        # loop though a range of 1 to target limit plus 1
        for i in range(1, target[-1] + 1):
            # if the output array is empty push the push the element into the stack
            if not output:
                output.append('Push')
                # if that element is not in the target array, pop it from the stack
                if i not in target:
                    output.append('Pop')
            # if element is in the target list, push into stack
            elif i in target:
                output.append('Push')
            # if the elment is not in the target list, first push it into the stack then pop it out immediatly
            else:
                output.append('Push')
                output.append('Pop')

        return output