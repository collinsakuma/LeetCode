from search_position import Solution

def test_answer():
    assert Solution().searchInsert([1,3,5,6], 5) == 2

def test_answer2():
    assert Solution().searchInsert([1,3,5,6], 2) == 1