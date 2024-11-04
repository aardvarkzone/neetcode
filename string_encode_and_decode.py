from typing import List

class Solution:
    
    def encode(self, strs: List[str]) -> str:
        temp = ''
        for string in strs: 
            temp += str(len(string)) + '&' + string
        return temp

    def decode(self, s: str) -> List[str]:
        output = []
        index = 0

        while index < len(s): 
            temp = index
            while s[temp] != '&': 
                temp += 1
            count = int(s[index:temp])
            index = temp + 1  
            output.append(s[index:index + count])
            index += count  
        return output
