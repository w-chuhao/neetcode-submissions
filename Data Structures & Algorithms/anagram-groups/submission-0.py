class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        mp = {}

        for i in range(len(strs)):
            s = tuple(sorted(strs[i]))

            if s not in mp:
                mp[s] = []
            
            mp[s].append(strs[i])

        
        return list(mp.values())
            

