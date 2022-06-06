
class Node:

    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data
    
class Solution:
    max_level = 0
    map = {}
    def tree_max_width(self,node: Node , level):
        if node is None: return

        if level > self.max_level:
            self.max_level = level
            
        self.tree_max_width(node.left , level + 1)

        self.tree_max_width(node.right , level + 1)  



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
print(driver.max_level)

