from find_first_occurrence import Solution

def test_answer():
    assert Solution().strStr("sadbutsad", "sad") == 0

def test_answer2():
    assert Solution().strStr("leetcode","code") == 5

def test_answer3():
    assert Solution().strStr("leetcode", "leeto") == -1