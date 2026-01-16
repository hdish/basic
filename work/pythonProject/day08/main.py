
from singlenode import SingleNode
from singleLinkedList import SingLinkeList


if __name__ == '__main__':
    # 创建节点类对象
    sn1 = SingleNode('山治')

    print(sn1.item)
    print(sn1.next)
    print('-' * 24)
    l = SingLinkeList(sn1)
    print(f'链表对象：{l}')
    print(f'链表的头结点：{l.head}')
    print(f'链表是否为空：{l.is_empty()}')
    print(f'链表长度为：{l.length()}')

    # 往头部加结点
    # l.add('路飞')
    # l.add('索隆')

    # 往尾部加结点
    l.append('路飞')
    l.append('索隆')

    # 往中间插
    # l.insert(-10,'艾斯')    # 相当于往头部加
    # l.insert(20,'马尔科')   # # 相当于往尾部加
    l.insert(1,'香克斯')

    # 删除
    # l.remove('王五')
    # l.remove('索隆')

    # 遍历列表
    l.travle()

    # 查
    print(l.search('路飞'))
    print(l.search('李四'))





