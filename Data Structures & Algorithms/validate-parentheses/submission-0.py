class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash = {')' : '(', '}' : '{', ']' : '['}
        for char in s:
            if char in hash:
                if not stack or stack[-1] != hash[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return not stack
        