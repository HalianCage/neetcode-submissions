class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s1 = {}

        for ch in s:
            s1[ch] = s1.get(ch, 0) + 1

        for ch in t:
            if ch not in s1 or s1[ch] == 0:
                return False
            s1[ch] -= 1

        return True

        