# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.
# constraint: -2^31 <= x <= 2^31 - 1
# Follow up: Could you solve it without converting the integer to a string? 

class Solution(object):
    def isPalindrome(self, x):
        string_x = str(x)
        string_y = string_x[::-1]
        return string_x == string_y 

x = -12321

solution = Solution()
print(solution.isPalindrome(x))