class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        #key is num, val is freq
        for num in nums: 
            if num not in hash_map: 
                hash_map[num] = 1
            else:
                hash_map[num] += 1
        
        sort = sorted(hash_map.items(), key=lambda item: item[1], reverse = True)
        return [item[0] for item in sort[:k]]
