def n_ways_step(n):
    
    if n==1: return 1
    if n==2: return 2

    return n_ways_step(n-1) + n_ways_step(n-2)


print(n_ways_step(4))