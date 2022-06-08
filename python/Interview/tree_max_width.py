
from queue import Queue

class Node:

    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data
    
class Solution:

    def tree_max_width(self,node: Node , level):
        max_width = 0
        q1 = Queue()
        marker = Node(-1)
        q1.put(node)
        q1.put(marker)
        while not q1.empty():
            current_node = q1.get()
            if(current_node == marker):
                q1.put(marker)
                print("marker found")
            else:
                print(current_node.data)
                q1.put(current_node.left)
                q1.put(current_node.right)




root = Node(1)
root.left = Node(2);
root.right = Node(3);
root.left.left = Node(4);
root.left.right = Node(5);
root.right.left = Node(6);
root.right.right = Node(7);
root.right.left.right = Node(8);
root.right.right.right = Node(9);
root.right.right.right.right = Node(12);

driver = Solution()
driver.tree_max_width(root , 1)
print(driver.max_width)

