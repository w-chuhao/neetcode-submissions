class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] > nums[r]:
                l = mid + 1

            else:
                r = mid

        min_index = l

        if nums[min_index] == target:
            return min_index

        if target > nums[-1]:
            l = 0
            r = min_index - 1

        else:
            l = min_index + 1
            r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                l = mid + 1

            else:
                r = mid - 1

        return -1