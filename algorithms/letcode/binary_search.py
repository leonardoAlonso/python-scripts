"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""
"""class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums)//2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            return self.search(nums[:mid + 1], target)
        if nums[mid] < target:
            return self.search(nums[mid - 1:], target)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums)-1, target)

    def binary_search(self, nums, start, end, target):
        center = (start + end) // 2
        if end < start:
            return -1
        if target == nums[center]:
            return center
        if target > nums[center]:
            return self.binary_search(nums, center + 1, end, target)
        if target < nums[center]:
            return self.binary_search(nums, start , center - 1, target)
        return -1
