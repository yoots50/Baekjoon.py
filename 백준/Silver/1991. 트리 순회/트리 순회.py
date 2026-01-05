def preorder(tree, root):
    if root == ".":
        return
    now = tree[root]
    print(root, end="")
    preorder(tree, now[0])
    preorder(tree, now[1])


def inorder(tree, root):
    if root == ".":
        return
    now = tree[root]
    inorder(tree, now[0])
    print(root, end="")
    inorder(tree, now[1])


def postorder(tree, root):
    if root == ".":
        return
    now = tree[root]
    postorder(tree, now[0])
    postorder(tree, now[1])
    print(root, end="")


def main():
    N = int(input())
    tree = {}
    for i in range(N):
        p, l, r = input().split()
        tree[p] = (l, r)

    preorder(tree, "A")
    print()
    inorder(tree, "A")
    print()
    postorder(tree, "A")


if __name__ == "__main__":
    main()
