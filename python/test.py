class Solution:
    keys  = {1 : "abc", 2 : "def", 3: "ghi"}
    def findDailer(self ,result,  level, nums):

        if len(nums) == level:
            print(result)
            return
        
        for i in self.keys[int(nums[level])]:
            result = result + i
            self.findDailer(result, level + 1 , nums)
            result = result[:-1]



driver  = Solution()

driver.findDailer('',0, '123')


