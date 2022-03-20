class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        二分查找，借助左右两个指针作为边界，L <= R 作为边界条件
        每次取中间值与目标值进行比较，未命中则调整左右边界直到 L>R
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (right-left)//2 + left
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        return -1

