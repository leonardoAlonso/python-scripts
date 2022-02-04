"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
https://leetcode.com/problems/search-insert-position/
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums)-1, target)
    
    def binary_search(self, nums, start, end, target):
        center = (start + end) // 2
        if end < start:
            return center+1
        if target == nums[center]:
            return center
        if target > nums[center]:
            return self.binary_search(nums, center + 1, end, target)
        if target < nums[center]:
            return self.binary_search(nums, start , center - 1, target)
        return center+1

