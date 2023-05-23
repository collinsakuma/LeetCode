from palindrom_number import Solution

def test_answer():
    solution = Solution()
    assert solution.isPalindrome(121) == True

def test_answer2():
    assert Solution().isPalindrome(122) == False

def test_answer3():
    assert Solution().isPalindrome(-121) == False