class BSTNode(object):
    def __init__(self,key,value=None,left=None,right=None):
        self.key = key
        self.value = value
        self.left = left 
        self.right = right
        

root = BSTNode(42) 
root.left = BSTNode(10)
root.right = BSTNode(90)
