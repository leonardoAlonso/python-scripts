from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        print(merged)
        mod = len(merged) % 2
        mid = len(merged) // 2
        if mod != 0:
            return merged[mid]
        return (merged[mid-1] + merged[mid]) / 2

if __name__ == '__main__':
    s = Solution()
    array1 = [1,2,3]
    array2 = [3,4,5]

    print(s.findMedianSortedArrays(array1, array2))