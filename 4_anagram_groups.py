class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_map = {}
        for string in strs:
            sort = ''.join(sorted(string))
            if sort not in hash_map:
                hash_map[sort] = []
            
            hash_map[sort].append(string)
            

        return list(hash_map.values())
