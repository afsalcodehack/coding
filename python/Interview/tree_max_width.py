
from queue import Queue

class Node:

    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data
    
class Solution:

    def tree_max_width(self,node: Node , level):
        max_width = 0
        width_count = 0
        q1 = Queue()
        marker = Node(-1)
        q1.put(node)
        q1.put(marker)
        while not q1.empty():
            current_node = q1.get()
            if current_node == marker:
                if width_count > max_width: max_width = width_count
                width_count = 0
            if current_node == marker and not q1.empty():
                q1.put(marker)
            else:
                width_count = width_count + 1
                print(current_node.data)
                if current_node.left is not None:
                    q1.put(current_node.left)
                if current_node.right is not None:
                    q1.put(current_node.right)
        print("max width = " , max_width)




root = Node(1)
root.left = Node(2);
root.right = Node(3);
root.left.left = Node(4);
root.left.right = Node(5);
root.right.left = Node(6);
# root.right.right = Node(7);
# root.right.left.right = Node(8);
# root.right.right.right = Node(9);
# root.right.right.right.right = Node(12);

driver = Solution()
driver.tree_max_width(root , 1)

