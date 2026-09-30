class Solution:
    
    def twosum(self, nums: list[int], target: int) -> list[int]:

        nums_index = {}

        for index, num in enumerate(nums):
            
            complement = target - num
             
            if complement in nums_index:
                return [nums_index[complement], index]
            nums_index[num] = index

        return []


nums = [13,6,9,15,4,5]

target = 20

soln = Solution()

print(soln.twosum(nums, target))