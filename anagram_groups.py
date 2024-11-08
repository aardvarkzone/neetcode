class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #hash_map with linked list 
        #key is sorted word, list holds anagrams 
        #to sort, use ''.join(sorted())
        #return list(hash_map.values())
        
        hash_map = {}

        for string in strs: 
            sorted_str = ''.join(sorted(string))
            if sorted_str not in hash_map:
                hash_map[sorted_str] = [] 
            
            hash_map[sorted_str].append(string)
        
        return list(hash_map.values())
