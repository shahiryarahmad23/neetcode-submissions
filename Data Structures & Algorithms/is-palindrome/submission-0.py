class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstring = ""

        for c in s:
            if c.isalnum():
                newstring += c.lower()
        if newstring == newstring[::-1]:
            return True
        else:
            return False
        