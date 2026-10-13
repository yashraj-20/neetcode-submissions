class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for elements in s:
            if elements not in Map:
                stack.append(elements)
                continue
            if not stack or stack[-1] != Map[elements]:
                return False
            stack.pop()

        return not stack

