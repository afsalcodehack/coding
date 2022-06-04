
class Node:

    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data
    
class Solution:
    sum = 0
    map = {}
    def vertical_sum(self,node: Node , level, target):
        if node is None: return

        if level == target:
            self.sum = self.sum + node.data
            
        self.vertical_sum(node.left , level-1 , target)

        self.vertical_sum(node.right , level+1 ,target)

    def vertical_sum_all(self,node: Node , level):
        if node is None: return

        if level in self.map:
            self.map[level] + self.map[level] + node.data
        else:
            self.map[level] = node.data
        
        self.sum = self.sum + node.data
            
        self.vertical_sum_all(node.left , level-1)

        self.vertical_sum_all(node.right , level+1)    

root = Node(1)
root.left = Node(2);
root.right = Node(3);
root.left.left = Node(4);
root.left.right = Node(5);
root.right.left = Node(6);
root.right.right = Node(7);
root.right.left.right = Node(8);
root.right.right.right = Node(9);

driver = Solution()
driver.vertical_sum(root , 0 , 3)
print(driver.sum)

driver.vertical_sum_all(root , 0)
print(driver.map)
