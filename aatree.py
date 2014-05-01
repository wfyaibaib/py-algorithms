from bst import *

class Aatree(Bst):
    def __init__(self, key_cmp = None):
        Bst.__init__(self, key_cmp)
        self.head.h = 0


    def insert_one_node(self, node, unique = False):
        node.color = False
        if not isinstance(node, Node):
            raise TypeError('Node Type required!')
        p = self.find_insert_positon(node)
        #         print 'newnode: %s, pos: %s' % (node, p)
        if p is self.head:
            self.head.p = node
            node.p = self.head
            self.cnt += 1
            self.insert_adjust(node)
            return node
        else:
            if unique:
                pre_node = p
                if self.key_cmp(node, p):
                    pre_node = self.prev(p)
                if pre_node is not self.head and not self.key_cmp(node, pre_node) and not self.key_cmp(pre_node, node):
                    return None
            node.p = p
            if self.key_cmp(node, p):
                p.l = node
            else:
                p.r = node
            self.cnt += 1
            self.insert_adjust(node)

            return node
