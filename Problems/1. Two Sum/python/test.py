from two_sum import Solution

def test_answer():
    assert Solution().twoSum([2,7,11,15],9) == [0,1]

def test_answer2():
    assert Solution().twoSum([3,2,4],6) == [1,2]

def test_answer3():
    assert Solution().twoSum([1,5,7,4,3,16,2],3) == [0,6]


    # class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     dict = {}
    #     for i, n in enumerate(nums):
    #         print(dict)
    #         print(n, i)
    #         if n in dict:
    #             return [dict[n], i]
    #         else:
    #             dict[target-n]=i

    # for test_answer3() if print statements where added after the for loop is initialized:
        # - on the first loop the dict is empty so it will execute the else condition adding 
        #   3 - 1: 0 to the dict n being 3 minus the target value of 2 at the index 0.
        # - on the second loop the dict now has a value of {2:0} n is now 5 and is not in the dict
        #   so the else condition is executed again adding 3 - 5: 1 to the dictionary. 
        # .......
        # - this continues untill the complement for n is found inside the dictionary. 