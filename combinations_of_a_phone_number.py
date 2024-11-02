class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        mapping = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        
        output = [""]

        for dig in digits: 
            temp = []
            for string in output:
                for char in mapping[dig]:
                    temp.append(string + char)
            output = temp
        return output

