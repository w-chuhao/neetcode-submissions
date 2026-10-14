class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        mid = (l+r)//2

        if nums[mid] == target:
            return mid

        while l<r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid
            
            elif nums[mid]>nums[r]:
                l = mid+1
            
            elif nums[mid]<nums[r]:
                r = mid

        min_index = l
        if nums[min_index]==target:
            return min_index

        if target>=nums[min_index] and target>=nums[-1]:
            r = min_index-1
            l = 0
            while l<=r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                if nums[mid]<target:
                    l = mid+1
                if nums[mid]>target:
                    r = mid-1

        if target>=nums[min_index] and target<=nums[-1]:
            l = min_index+1
            r = len(nums)-1
            while l<=r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                if nums[mid]<target:
                    l = mid+1
                if nums[mid]>target:
                    r = mid-1

        return -1
                



            
            