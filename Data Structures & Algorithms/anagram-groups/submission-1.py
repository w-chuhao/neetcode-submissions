class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        mp = {}

        for word in strs:
            count = [0] * 26

            for char in word:
                index = ord(char) - ord("a")
                count[index] += 1
            
            key = tuple(count)

            if key not in mp:
                mp[key] = []
            
            mp[key].append(word)

        return list(mp.values())
            

