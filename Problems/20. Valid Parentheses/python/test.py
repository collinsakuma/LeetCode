from valid_parentheses import Solution

def test_answer():
    assert Solution().isValid("(){}[]") == True

def test_answer2():
    assert Solution().isValid("(])") == False

def test_answer3():
    assert Solution().isValid("({})") == True