import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-z0-9]', '', s.lower())
        return s==s[::-1]

# remove commas , spaces 
#lowercase everything
#store original wala and compare it with reverse wala
# to rev => str[::-1]

        