from remove_dup_from_sorted_array import Solution

def test_answer():
    test_list = [1,1,2]
    expected_answer = 2
    assert Solution().removeDuplicates(test_list) == expected_answer
    assert Solution().removeDuplicatesTwoPointer(test_list) == expected_answer

def test_answer2():
    test_list = [1,1,1,2,3,3,4,4,4,5,5,5]
    expected_answer = 5
    assert Solution().removeDuplicates(test_list) == expected_answer
    assert Solution().removeDuplicatesTwoPointer(test_list) == expected_answer