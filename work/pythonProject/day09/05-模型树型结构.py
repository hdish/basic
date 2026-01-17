
#1．定义类Node，表示：节点。
class Node:
    #初始化属性
    def __init__(self, item):
        self.item = item        # 节点的内容
        self.lchild = None      # 左子树
        self.rchild = None      # 右子树

#2．定义BinaryTree类，表示：二叉树。
class BinaryTree:
    #初始化属性
    def __init__(self, root=None):
        self.root = root    #root表示：根节点.

    #自定义函数add，表示往：二叉树中添加元素。
    def add(self, item):
        if self.root is None:
            self.root = Node(item)
            return

        queue = []
        queue.append(self.root)

        while True:
            root_node = queue.pop(0)
            if root_node.lchild is None:
                root_node.lchild = Node(item)
                break
            else:
                queue.append(root_node.lchild)

            if root_node.rchild is None:
                root_node.rchild = Node(item)
                break
            else:
                queue.append(root_node.rchild)


    #自定义函数breadth_travel（self），表示：遍历二叉树，获取每个元素，广度优先。
    def breadth_travel(self):
        # 1，判断根节点是否为空，如果为空，直接返回即可.
        if self.root is None:
            return
        # 2.走到这里，说明根节点不为空，创建队列，把根节点加入队列
        queue =[]
        queue.append(self.root)
        # 3.具体的获取元素的动作，只要队列中有元素，我们就一直获取
        while len(queue) > 0:
            # 4.打印当前节点的信息.
            node = queue.pop(0)
            print(node.item, end=' ')
            # 5，判断当前节点左子树，如果不为空，就添加到队列中，
            if node.lchild is not None:
                queue.append(node.lchild)
            # 6，判断当前节点右子树，如果不为空，就添加到队列中.
            if node.rchild is not None:
                queue.append(node.rchild)


    # 自定义函数 preorder_traveL（self），表示：遍历二叉树，获取每个元素，深度优先-前序
    def preorder_travel(self,root):  # 根左右  root是传入的结点
        if root is not None:
            print(root.item, end=' ')  # 根
            self.preorder_travel(root.lchild)  # 递归获取，左子树
            self.preorder_travel(root.rchild)  # 递归获取，右子树


    # 自定义函数inorder_travel（self），表示：遍历二叉树，获取每个元素，深度优先-中序
    def inorder_travel(self,root):  # 左根右  root是传入的结点
        if root is not None:
            self.inorder_travel(root.lchild)  # 递归获取，左子树
            print(root.item, end=' ')  # 根
            self.inorder_travel(root.rchild)  # 递归获取，右子树


    # 自定义函数postorder_travel（self），表示：遍历二叉树，获取每个元素，深度优先-后序
    def postorder_travel(self,root):  # 左右根  root是传入的结点
        if root is not None:
            self.postorder_travel(root.lchild)  # 递归获取，左子树
            self.postorder_travel(root.rchild)  # 递归获取，右子树
            print(root.item, end=' ')  # 根
# def demo01_测试节点和链表创建():  # 创建节点对象.
#     node = Node('乔峰')
#     print(f'节点的内容：{node.item}')
#     print(f'节点的左子树：{node.lchild}')
#     print(f'节点的右子树：{node.rchild}')
#     # 测试二叉树对象，
#     bt = BinaryTree(node)
#     print(f'二叉树对象：{bt}')
#     print(f'二叉树的根节点的内容：{bt.root.item}')


# def demo02_广度优先():
#     # 创建二叉树
#     bt = BinaryTree()
#     # 添加元素
#     bt.add('A')
#     bt.add('B')
#     bt.add('C')
#     bt.add('D')
#     bt.add('E')
#     bt.add('F')
#     bt.add('G')
#     bt.add('H')
#     bt.add('I')
#     bt.add('J')
#
#     bt.breadth_travel()

def demo03_深度优先():
    # 创建二叉树
    bt = BinaryTree()
    # 添加元素
    bt.add(0)
    bt.add(1)
    bt.add(2)
    bt.add(3)
    bt.add(4)
    bt.add(5)
    bt.add(6)
    bt.add(7)
    bt.add(8)
    bt.add(9)

    # bt.preorder_travel(bt.root)
    # bt.inorder_travel(bt.root)
    bt.postorder_travel(bt.root)

if __name__ == '__main__':
    # demo01_测试节点和链表创建()
    # demo02_广度优先()
    demo03_深度优先()