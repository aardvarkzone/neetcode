class TimeMap:

    def __init__(self):
        self.set_dict = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.set_dict: 
            self.set_dict[key] = []
        self.set_dict[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        output = ""                       
        strings = self.set_dict.get(key, [])  
        left = 0
        right = len(strings) - 1

        while left <= right: 
            middle = left + (right - left) // 2  
            if strings[middle][1] <= timestamp: 
                output = strings[middle][0]      
                left = middle + 1               
            else: 
                right = middle - 1              
        
        return output                          
