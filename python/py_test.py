
def solution(A):
    max = 1 
    A.sort()
    prev = A[0]
    if A[len(A)-1] < 1 : return 1
    isFound = False
    for i in A:
        if i > prev+1:
            max  = prev + 1
            isFound = True
            break
        prev = i    
    return max if isFound else A[len(A)-1]+1



print(solution([1, 3, 6, 4, 1, 2]))
print(solution([1, 2, 3]))
print(solution([-1,  -3]))
