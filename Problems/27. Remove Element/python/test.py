from remove_element import Solution

def test_answer():
    assert Solution().removeElement([3,2,2,3], 3) == 2

def test_answer2():
    assert Solution().removeElement([0,1,2,2,3,0,4,2], 2) == 5