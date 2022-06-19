
from ast import Is
from queue import Queue

class Node:

    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data
    
class Solution:
    level_count = {}
    def print_left_view(self,node: Node, level):

        if node is None:
            return
        if level not in self.level_count:
            print(node.data)
            self.level_count[level] = True
        
        self.print_left_view(node.left, level+1)
        self.print_left_view(node.right, level+1)
        




# root = Node(4)
# root.left = Node(5);
# root.right = Node(2);
# root.right.left = Node(3);
# root.right.right = Node(1);
# root.right.left.left = Node(6);
# root.right.left.right = Node(7)


root = Node(1)
root.left = Node(2);
root.right = Node(3);
root.left.right = Node(4);
root.left.right.right = Node(5);
root.left.right.right.right = Node(6);

driver = Solution()
driver.print_left_view(root, 0)

