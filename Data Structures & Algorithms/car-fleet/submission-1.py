class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []

        if not position:
            return 0

        for i in range(len(position)):
            arr.append([position[i],speed[i]])
        
        arr.sort(reverse=True)

        time = []
        speed = arr[0][1]
        dist = target - arr[0][0]
        t = dist / speed
        time.append(t)
        
        count = 0

        for i in range(1, len(arr)):
            speed = arr[i][1]
            dist = target - arr[i][0]

            t = dist / speed

            if t<=time[count]:
                continue
            else:
                time.append(t)
                count+=1

        return len(time)