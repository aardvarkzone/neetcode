class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #make a hashmap - key: num, value: index
        #find comp = target - num 
        #   - if comp in hash_map, return [hash_map[num], index]
        #   - else, hash_map[num] = index
        #no matches = []
        #hash_map[comp] < index because if its is in hash_map, it must've been a previous index
        hash_map = {}
        for index, num in enumerate(nums): 
            comp = target - num
            if comp in hash_map:
                return[hash_map[comp], index]
            hash_map[num] = index

        
        return []
