root1 = [3,9,20, None,None,15,7]

root2 = [3,9,20,15,7]
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        quene = []  # we use first in first out quene for Breadth-First-search
        res = []
        quene.append(root)
        
        while(quene):   # loop through every level
            print(quene, len(quene))
            qlen = len(quene)   # how many elements in the current row
            tmp = 0
            for i in range(qlen):   # loop through elements in current level
                node = quene.pop(0)
                tmp += node.val
                if node.left:   
                    quene.append(node.left)
                if node.right:
                    quene.append(node.right)
            res.append(tmp/qlen)    # calculate the average 
        
        return res


hi = TreeNode()
hi.averageOfLevels(root2)

