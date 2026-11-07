class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mp = {}

        for char in s:
            if char not in mp:
                mp[char] = mp.get(char,0)+1
            else:
                mp[char]+=1
            
        for char in t:
            if char in mp:
                mp[char]-=1
            
            if char not in mp:
                return False

            if mp[char]<0:
                return False
        return True



        