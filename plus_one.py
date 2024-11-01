class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = ''
        for digit in digits: 
            temp += str(digit)
        temp_int = int(temp)
        temp_int += 1
        output = []
        for digit in str(temp_int):
            output.append(int(digit))

        return output
        
