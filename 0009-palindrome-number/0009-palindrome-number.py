class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        org = x
        if x < 0:
            return False
        elif x>=0:
            while x > 0:
                k = x % 10
                x = x // 10
                rev = rev * 10 + k
            if rev == org:
                return True
            else:
                return False
