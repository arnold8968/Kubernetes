class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(nums)-1
        while start+1 < end:
            mid = start + (end-start)//2
            if nums[mid] == target:
                break
            if nums[mid] > target:
                end = mid
            else:
                start = mid
        return mid
a = Solution()
print(a.searchRange([5,7,7,8,8,10],8))