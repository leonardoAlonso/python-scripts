"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

https://leetcode.com/problems/two-sum
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = 0
        diferences = {}
        length = len(nums)
        while(index < length):
            n = nums[index]
            if (diferences.get(target-n)):
                return [diferences[target-n]['index'], index]
            diferences[n] = {
                'value': target - n,
                'index': index
            }
            index += 1
        return []

