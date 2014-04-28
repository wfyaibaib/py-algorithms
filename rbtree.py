from bst import *

class Rbtree(Bst):
    def __init__(self, key_cmp = None):
        #super(Rbtree, self).__init__(key_cmp)
        Bst.__init__(self, key_cmp)
        self.head.color = True

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


    def insert_adjust(self, node):
        if node.p is self.head:
            node.color = True
            return
        else:
            node.color = False
            if parent(node).color is True:
                return
            else:
                p = parent(node)
                pp = parent(p)
                u = uncle(node)
                if u.color is False:
                    p.color = u.color = True
                    pp.color = False
                    self.insert_adjust(pp)
                else:
                    if p is left(pp):
                        if node is right(p):
                            self.left_rotation(p)
                            self.right_rotation(pp)
                            pp.color = False
                            node.color = True
                        else:
                            self.right_rotation(pp)
                            pp.color = False
                            p.color = True
                    else:
                        if node  is left(p):
                            self.right_rotation(p)
                            self.left_rotation(pp)
                            pp.color = False
                            node.color = True
                        else:
                            self.left_rotation(pp)
                            pp.color = False
                            p.color = True

    def delete_one_node(self, node):

        d = delete = node
        if left(delete) is not self.head and right(delete) is not self.head:
            d = bst_successor(delete, self.head)
            delete.copy_data_from(d)
        n = left(d) if self.head is right(d) else right(d)
        p = parent(d)
        if d is left(p):
            p.l = n
        elif d is right(p):
            p.r = n
        else:
            p.p = n
        if n is not self.head:
            n.p = p
        dc = d.color
        self.cnt -= 1
        del d


        if dc is True:
            self.delete_adjust(n, p)

    def node_str(self, node):
        return '(%s, %s)' % (node.data, 'b' if node.color else 'r')
    def delete_adjust(self, node, node_parent):

        n = node
        np = node_parent
        if (self.empty()):
            return
        else:
            if n.color is False:
                n.color = True
                return
            else:
                while True:
#                     print 'inloop'
                    if n is self.root():
                        if n.color is False:
                            n.color = True
                        return
                    p = np if n is self.head else parent(n)
                    s = right(p) if n is left(p) else left(p)
                    sl = left(s)
                    sr = right(s)
                    help_dic = {True: 1, False: 0}
                    state = help_dic[p.color]*8 + help_dic[s.color]*4 + help_dic[sl.color]*2 + help_dic[sr.color]
                    if state == 11:
                        if n is left(p):
                            self.left_rotation(p)
                            s.color = True
                            sl.color = False
                        else:
                            self.right_rotation(p)
                            s.color = True
                            sr.color = False
                        return
                    elif state == 15:
                        s.color = False
                        n = p
                        continue
                    elif state == 7:
                        p.color = True
                        s.color = False
                        return
                    else:
                        if n is left(p):
                            if state == 5 or state == 13:
                                self.right_rotation(s)
                                self.left_rotation(p)
                                sl.color = p.color
                                p.color = True
                                return
                            elif state in [4, 6, 12, 14]:
                                self.left_rotation(p)
                                s.color = p.color
                                p.color = True
                                sr.color = True
                                return
                        else:
                            if state == 6 or state == 14:
                                self.left_rotation(s)
                                self.right_rotation(p)
                                sr.color = p.color
                                p.color = True
                                return
                            if state in [4, 5, 12, 13]:
                                self.right_rotation(p)
                                s.color = p.color
                                p.color = True
                                sl.color = True
                                return

    def dot_node_option(self, node):
        return {"color": "black" if node.color else "red"}

if __name__ == '__main__':
    class TestNode(Node):
        def __str__(self):
            return '(%s, %s)' % (self.data, 'b' if self.color else 'r')
    tree = Rbtree()
    for i in range(6):
        tree.insert_one_node(TestNode(data = i))
    tree.tree_shape()

    for i in range(6):
#         print 'del:' , i
        tree.delete_one_node(tree.root())
        tree.tree_shape()
    #tree.render('rbtree')
