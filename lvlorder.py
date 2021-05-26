from collections import deque

"""Class Binary Tree"""
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None



#Level Order Traversal using queue

def lvlorder(rootnode):
    if rootnode is None:
        return "No node found"
    
    q=deque()
    
    q.append(rootnode)
    
    while len(q)!=0:
        p=q.popleft()
        print(p.data)
        if p.leftchild is not None:
            q.append(p.leftchild)
            
        if p.rightchild is not None:
            q.append(p.rightchild)



"""Driver Code"""


"""Root node(Parent)"""
newBT=TreeNode("Drinks")

"""Childs"""
h=TreeNode("hot")
c=TreeNode("cold")
cofee=TreeNode("coffee")
cola=TreeNode("Coca Cola")

newBT.leftchild=h
newBT.rightchild=c

h.leftchild=cofee
c.leftchild=cola

lvlorder(newBT)