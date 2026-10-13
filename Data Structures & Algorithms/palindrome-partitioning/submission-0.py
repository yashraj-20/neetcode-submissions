class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def backtracking(start, curr):
            if start == len(s):
                result.append(curr[:])
                return
            
            for i in range(start+1, len(s)+1):
                part = s[start:i]
                if part == part[::-1]:
                    curr.append(part)
                    backtracking(i, curr)
                    curr.pop()
        
        backtracking(0, [])
        return result