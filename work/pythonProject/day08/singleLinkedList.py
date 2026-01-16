
from singlenode import SingleNode

class SingLinkeList(object):
    # 初始化属性，用 head 属性，指向：链表的头结点
    def __init__(self,node=None):
        self.head = node

    # 判断链表是否为空
    def is_empty(self):
        # # 方法1
        # if self.head == None:
        #     return True
        # else:
        #     return False

        # # 方法2 三元
        # return True if self.head == None else False

        # 方法3
        return self.head == None

    # 计算链表长度
    def length(self):
        count = 0
        current = self.head
        # while current != None:
        while current is not None:
            count += 1
            current = current.next
        return count

    # 遍历列表
    def travle(self):
        current = self.head
        while current is not None:
            print(current.item)
            current = current.next

    # add（self，item）链表头部添加元素
    def add(self,item):
        # 把item封装成新结点
        new_node = SingleNode(item)
        # 设置 新结点的 地址域 指向 之前的头结点
        new_node.next = self.head
        #  设置 头结点 指向 新结点
        self.head = new_node

    # append（self，item）链表尾部添加元素
    def append(self,item):
        # 把item封装成新结点
        new_node = SingleNode(item)
        # 判断链表是否为空，如果为空新结点当头结点即可
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    # insert（self，pos，item） 指定位置添加元素
    def insert(self,pos,item):
        """
        指定位置添加元素
        :param pos: 要添加元素到的 位置(索引)
        :param item: 具体添加的新结点
        :return:
        """
        # pos<0,往头部添加
        if pos <= 0:
            self.add(item)
        # pos>链表的长度，往尾部添加
        elif pos >= self.length():
            self.append(item)
        else:
            # count 是插入位置 前面的元素 的 索引
            count = 0
            # 插入位置前的结点
            current = self.head
            # 将count定位到 插入位置 前面的元素
            while count < pos - 1:
                # count往前加1
                count += 1
                # 结点跟新为下一个结点
                current = current.next
            # 创建要插入的结点
            new_node = SingleNode(item)
            # 新结点的地址域 指向 插入位置前的结点的地址域
            new_node.next = current.next
            # 插入位置前的结点的地址域 指向 新结点
            current.next = new_node

    # remove（self，item） 删除节点
    def remove(self,item):
        # 当前结点默认指向头结点
        current = self.head
        # 当前结点的前一个结点
        pre = None
        # 遍历 每个结点
        while current is not None:
            # 判断是不是要删除的结点
            if current.item == item:
                # 判断删除的是不是头结点
                if current == self.head:
                    # 是的话 头结点 指向 原头结点 的 下一个结点
                    self.head = current.next
                else:
                    # 要删除的不是头结点
                    pre.next = current.next
                break
            else:
                # 判断过不是的结点 给上一个结点
                pre = current
                # 当前结点跟新为下一个结点
                current = current.next

    # search（seLf，item）查找节点是否存在
    def search(self,item):
        current = self.head
        # 遍历每个结点
        while current is not None:
            # 判断是否要查找的结点
            if current.item == item:
                # 是的话返回True
                return True
            else:
                # 跟新为下个结点
                current = current.next
        # while都结束了，即:没有找到
        return False