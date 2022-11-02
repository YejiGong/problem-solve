N = int(input())
tree={}

class Node():
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right
        
for _ in range(N):
    root, l, r = map(str,input().split())
    tree[root]=Node(root,l,r)

def preorder(node):
    print(node.item, end='')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])
        
def inorder(node):
    if node.left != '.':
        inorder(tree[node.left])
    print(node.item, end='')
    if node.right != '.':
        inorder(tree[node.right])
        
def postorder(node):
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.item, end='')

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])

