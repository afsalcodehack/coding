from queue import PriorityQueue


q = PriorityQueue()

q.put(4)
q.put(2)
q.put(5)
q.put(1)
q.put(3)

print(q.get())
print(q.get())
print("this is a test")
print("somthin went wrong")
