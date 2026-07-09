class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        '''
        TEST ALGORITHM:- TWO POINTER APPROACH
        Step 1: initialize two pointers at the start of the string
        Step 2: Update the right pointer one by one and keep adding each new character to the memSet
        Step 3: The position difference of the two pointers would be the length, which is updated and stored in maxCount
        Step 4: when a duplicate character is encountered, update the left pointer until it reaches one position ahead of the first appearance of that duplicate character
        Step 5: While updating the left pointer in the above step, make sure to remove each character from the memSet
        Step 6: continue this process until the end of string is reached
        '''

        l, r = 0, 0
        maxCount = 0
        memSet = set()

        while r < len(s):
            ch = s[r]
            if ch not in memSet:
                diff = r-l+1
                maxCount = max(maxCount, diff)
                memSet.add(ch)
                r += 1
            else:
                while l <= r and s[l] != ch:
                    memSet.remove(s[l])
                    l += 1
                l += 1
                diff = r-l+1
                maxCount = max(maxCount, diff)
                r += 1

        return maxCount




        