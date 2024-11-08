class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #unique solution
        #hash: key = num in nums, value = count of key
        #sort by count (non-ascending), return list of first k elems
        #use .items() to get (key, value) pairs for sort (item[1] = value)

        #notes: lambda = function collapse
        #list slicing:
            # [start:stop] start is inclusive, stop is exclusive
            # [:] entire list copy (shallow)
            # [::step] every step element
            # [::-1] reverse the list
            # [-n:] last n elements
            # [n:] from index n to the end
            # [:n] first n elements excluding index n
            # [:-n] all elements except the last n

        hash_map = {}

        for num in nums: 
            if num in hash_map: 
                hash_map[num] += 1
            else: 
                hash_map[num] = 1
        
        sorted_hash = sorted(hash_map.items(), key = lambda item: item[1])
        return [item[0] for item in sorted_hash[-k:]]
