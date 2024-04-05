#28. Find the Index of the First Occurrence in a String
#Input: haystack = "sadbutsad", needle = "sad"
#Output: 0
#Explanation: "sad" occurs at index 0 and 6.
#The first occurrence is at index 0, so we return 0.


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) <= 0: return -1
        first_index = -1
        for i in range(0, len(haystack)):
            h_index = i
            needle_index  = 0;

            if first_index != -1:
                break

            while h_index < len(haystack) and needle_index  < len(needle):
                # print(haystack[h_index] , needle[needle_index])
                if haystack[h_index] == needle[needle_index]:
                    if len(needle) == h_index: 
                        break 
                    if first_index == -1 : first_index  = i
                    
                    h_index = h_index + 1
                    needle_index = needle_index +1
                else:
                    first_index  = -1;
                    break;

        return first_index


service = Solution()
print(service.strStr("affsasal","sal")) #5
print(service.strStr("sadbutsad","but")) #3
print(service.strStr("sadbutsad","buta")) #-1
print(service.strStr("sadbutsad","")) #-1
print(service.strStr("mississippi","issip")) #4