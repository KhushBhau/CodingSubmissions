class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        neg = x < 0
        x = abs(x)
        while x > 0:
            k = x % 10
            x = x // 10
            rev = rev * 10 + k
        if neg:
            rev = -rev
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        
        return rev

        return rev
