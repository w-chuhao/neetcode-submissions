class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for char in s:
            if char in matches:  # closing bracket
                if not stack or stack.pop() != matches[char]:
                    return False
            else:  # opening bracket
                stack.append(char)

        return not stack