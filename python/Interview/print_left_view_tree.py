
from queue import Queue

class Node:

    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data
    
class Solution:

    def print_left_view(self,node: Node):
        q1 = Queue()
        marker = Node(-1)
        q1.put(node)
        q1.put(marker)
        isMarker = True
        while not q1.empty():
            current_node = q1.get()

            if isMarker == True:
                print(current_node.data)
                isMarker = False

            if current_node == marker and not q1.empty():
                isMarker = True
                q1.put(marker)
            else:

                if current_node.left is not None:
                    q1.put(current_node.left)
                if current_node.right is not None:
                    q1.put(current_node.right)




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
driver.print_left_view(root)

