from roman_to_integer import Solution

def test_answer():
    assert Solution().romanToInt("III") == 3

def test_answer2():
    assert Solution().romanToInt("LVIII") == 58