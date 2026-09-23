class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        mp1 = {}
        for i in range(len(s1)):
            mp1[s1[i]] = mp1.get(s1[i],0)+1

        left = 0
        right = 0
        window_size = len(s1)

        mp2 = {}

        for right in range(len(s2)):
            mp2[s2[right]] = mp2.get(s2[right],0) + 1

            if right-left>window_size-1:
                mp2[s2[left]] = mp2.get(s2[left]) - 1

                if(mp2[s2[left]]==0):
                    mp2.pop(s2[left])
                left+=1
            
            if mp2==mp1:
                return True
        
        print(mp1)
        print(mp2)


        return False
        