class Solution:
    def isPalindrome(self, s: str) -> bool:

        # string = ''.join([ch for ch in s if ch.isalnum()])
        start = 0
        end = len(s)-1

        while start < end:

            if not s[start].isalnum():
                while start < len(s) and not s[start].isalnum():
                    start += 1
                continue

            if not s[end].isalnum():
                while end > -1 and not s[end].isalnum():
                    end -= 1
                continue

            if s[start].lower() != s[end].lower():
                return False
            
            start += 1
            end -= 1

        return True
        