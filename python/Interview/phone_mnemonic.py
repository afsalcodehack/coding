
class Solution:
    dailer = {1 : [], 2: 'abc' , 3: 'def' , 4: 'ghi' , 5: 'jkl' ,6: 'mno' ,
        7 : 'pqrs', 8: 'tuv' , 9 : 'xyz' , 0 :'' }

    def dailer_recursion(self,num , result):
        if len(num) == len(result):
            print(result)
            return
        
        for i in num:
            for j in self.dailer[int(i)]:
                result  = result + j
                self.dailer_recursion(num , result)


driver = Solution()
driver.dailer_recursion('23', '')


