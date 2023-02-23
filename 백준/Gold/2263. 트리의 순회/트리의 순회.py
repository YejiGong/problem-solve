import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n= int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))

node = [0]*(n+1)
for i in range(n):
    node[inorder[i]] = i

def preorder(inS, inE, postS, postE):
    if (inS>inE) or (postS>postE):
        return
    root = postorder[postE]

    leftnode = node[root] - inS
    rightnode = inE - node[root]

    print(root, end=" ")
    preorder(inS, inS+leftnode-1, postS, postS+leftnode-1)
    preorder(inE-rightnode+1, inE, postE-rightnode, postE-1)

preorder(0, n-1, 0, n-1)


