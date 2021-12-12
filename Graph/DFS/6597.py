import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def postorder(preorder, inorder):
    global answer
    if not preorder:
        return
    root = preorder[0]
    l = inorder.index(root)
    postorder(preorder[1:l+1], inorder[:l])
    postorder(preorder[l+1:], inorder[l+1:])
    answer += root


while True:
    try:
        po, io = map(str, input().split())
        answer = ""
        postorder(po, io)
        print(answer)
    except:
        break
