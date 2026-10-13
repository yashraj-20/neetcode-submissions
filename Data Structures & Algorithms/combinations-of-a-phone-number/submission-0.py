class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        # print(digitToChar["2"][0])
        result = []
        def backtracking(index, curr):
            if index == len(digits):
                result.append("".join(curr))
                return
            
            for i in range(len(digitToChar[digits[index]])):
                curr.append(digitToChar[digits[index]][i])
                backtracking(index+1, curr)
                curr.pop()
            
        backtracking(0, [])
        return result