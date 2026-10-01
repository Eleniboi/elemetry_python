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

def selection_sorting(nums):
    # Loop through the entire list
    for i in range(len(nums)):
        # Assume the current position holds the smallest number
        smallest_idx = i
        
        # Check the rest of the list to find a truly smaller number
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[smallest_idx]:
                smallest_idx = j
                
        # Swap the found smallest element with the current element
        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]
        
    return nums

nums = [4, 6, 9, 15, 7, 3]
print(selection_sorting(nums))  # Output: [3, 4, 6, 7, 9, 15]
