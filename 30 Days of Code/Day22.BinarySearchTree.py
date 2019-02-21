class Node: # an object eg.house
    def __init__(self,data):
        self.right=self.left=None # pointer = address eg.2 piece of blank paper in the house
        self.data = data # data of this house, eg.n floors
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data) # create a house with n rooms, 2 pieces of blank paper to hold addresses 
        else:
            if data<=root.data: # if fewer rooms than this house
                cur=self.insert(root.left,data) # find the empty address on the left paper to build the house
                root.left=cur # write down this address on last houses paper
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root # return this house

    def getHeight(self,root):
        #Write your code here
        if root == None:
            return -1
        else:
            left = 1 + self.getHeight(root.left)
            right = 1 + self.getHeight(root.right)
        return max(left,right)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       