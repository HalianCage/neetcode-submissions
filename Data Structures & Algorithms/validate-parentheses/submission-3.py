class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 1:
            return False

        stack = []

        mp = {')':'(', '}':'{', ']':'['}

        for c in s:

            if c in ('(', '{', '['):
                stack.append(c)
            
            elif len(stack) != 0:
                if stack[-1] == mp[c]:
                    stack.pop()
                else:
                    return False
            else:
                return False

        if len(stack) == 0:
            return True
        else:
            return False
                
        