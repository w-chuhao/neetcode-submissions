class TimeMap:

    def __init__(self):
        self.mp = {}


        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key] = []
            
        self.mp[key].append([value,timestamp])

    
    def get(self, key: str, timestamp: int) -> str:

        val = ""
        if key not in self.mp:
            return val

        result = self.mp.get(key)

        l=0
        r=len(result)-1

        while l<=r:
            mid = (l+r)//2

            if result[mid][1] == timestamp:
                return result[mid][0]

            if result[mid][1] < timestamp:
                l = mid+1
                val = result[mid][0]
            
            if result[mid][1] > timestamp:
                r = mid-1
        
        return val
        
