 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#TC = O(N)
#SC = O(H)
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        self.result = []
        self.dfs(root,0)
        return self.result
    
    def dfs(self, root: Optional[TreeNode], lvl : int) ->None:
        if root == None:
            return

        if(lvl == len(self.result)):
            #temp = []
            #temp.append(root.val)
            self.result.append(root.val)
        else:
            self.result[lvl] = root.val
        
        self.dfs(root.left, lvl + 1)
        self.dfs(root.right, lvl + 1)
        
        