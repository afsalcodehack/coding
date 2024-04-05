class Solution:
    def next_permutation(self, nums) -> None:
        is_swapped = False
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                is_swapped = True
                temp = nums[i]
                nums[i] = nums[i - 1]
                nums[i - 1] = temp
                break

        if not is_swapped:
            nums.sort()
        print(nums)


service = Solution()

print(service.nextPermutation([1, 2, 3]))
print(service.nextPermutation([3, 2, 1]))
print(service.nextPermutation([1, 1, 5]))
print(service.nextPermutation([1, 3, 2]))  # [2,1,3]
