class Solution:
    def isPalindrome(self, s: str) -> bool:

        string = ''.join([ch for ch in s if ch.isalnum()])
        start = 0
        end = len(string)-1

        while start < end:
            if string[start].lower() != string[end].lower():
                return False
            
            start += 1
            end -= 1

        return True
        