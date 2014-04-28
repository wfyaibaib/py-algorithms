from node import *
class Bst:
    def __init__(self, key_cmp = None):
        self.cnt = 0
        self.head = Node()
        self.head.l = self.head.r = self.head.p = self.head
        self.head.data = -1

        def node_cmp(x, y):
            if not isinstance(x, Node) or not isinstance(y, Node):
                raise TypeError("Must be Node type")
            else:
                #print '%s cmp %s' % (x, y)
                return x.data < y.data

        self.key_cmp = key_cmp
        if key_cmp is None:
            self.key_cmp = node_cmp

    def size(self):
        return self.cnt

    def root(self):
        return parent(self.head)

    def left_most(self):
        return bst_left_most(self.root(), self.head)

    def right_most(self):
        return bst_right_most(self.root(), self.head)

    def right_rotation(self, node):
        bst_right_rotation(node, self.head)

    def left_rotation(self, node):
        bst_left_rotation(node, self.head)

    def is_root(self, node):
        return parent(node) is self.head

    def empty(self):
        return self.size() == 0

    def node_str(self, node):
        return str(node)

    def node_shape_recusive(self, subtree, table_cnt = 0):
        delimiter = table_cnt * '\t'
        if subtree is self.head:
            print delimiter + "[None]"
        else:
            self.node_shape_recusive(right(subtree), table_cnt + 1)
            print delimiter + self.node_str(subtree)
            self.node_shape_recusive(left(subtree), table_cnt + 1)

    def tree_shape(self):
        self.node_shape_recusive(self.root())

    def next(self, node):
        return bst_successor(node, self.head)

    def prev(self, node):
        return bst_predecessor(node, self.head)

    def minium(self):
        if not self.empty():
            return self.left_most()
        else:
            return self.head

    def maximum(self):
        if not self.empty():
            return self.right_most()
        else:
            return self.head

    def find_insert_positon(self, node):
        node.l = node.r = self.head
        return bst_find_insert_position(self.root(), node, self.head, self.key_cmp)

    def insert_one_node(self, node, unique = False):
        if not isinstance(node, Node):
            raise TypeError('Node Type requered')
        p = self.find_insert_positon(node)
#         print 'newnode: %s, pos: %s' % (node, p)
        if p is self.head:
            self.head.p = node
            node.p = self.head
            self.cnt += 1
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
            return node

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
        del d
        self.cnt -= 1

    def __iter__(self):
        if self.empty():
            yield None
        else:
            each = self.left_most()
            while each is not self.head:
                yield each
                each = self.next(each)

    def insert_data_list(self, data_list, unique = False):
        for data in data_list:
            node = Node(data = data)
            self.insert_one_node(node, unique = False)

    def insert_data(self, data, unique = False):
        node = Node(data = data)
        self.insert_one_node(node, unique = False)

    def dot_node_option(self, node):
        return {}

    def render(self, dot_file_name, dot_format = 'png'):
        if self.empty():
            return
        from graphviz import Digraph
        dot = Digraph()

        root = self.root()
        dot.format = dot_format

        def all_nodes_and_edges(subtree):
            dot.node(subtree.name, label = subtree.label, **self.dot_node_option(subtree))
            if subtree.l is not self.head:
                dot.edge(subtree.name, subtree.l.name)
                dot.edge(subtree.l.name, subtree.name)
                all_nodes_and_edges(subtree.l)

            else:
                null = Node()
                dot.node(null.name, label = 'null')
                dot.edge(subtree.name, null.name)
            if subtree.r is not self.head:
                dot.edge(subtree.name, subtree.r.name)
                dot.edge(subtree.r.name, subtree.name)
                all_nodes_and_edges(subtree.r)
            else:
                null = Node()
                dot.node(null.name, label = 'null')
                dot.edge(subtree.name, null.name)

        all_nodes_and_edges(root)
        dot.render(dot_file_name)



if __name__ == '__main__':
    tree = Bst(key_cmp = lambda x, y: x.data > y.data)
    for i in range(3):
        node1 = tree.insert_one_node(Node(data = 1))
        node2 = tree.insert_one_node(Node(data = 2))
        node3 = tree.insert_one_node(Node(data = 3))

    tree.tree_shape()
    for i in tree:
        print i

#     tree.delete_one_node(node1)
    l = [1, 2, 3, 4, 5, 6]
    tree.insert_data_list(l)
    tree.tree_shape()
    cnt = tree.size()
    for i in range(cnt):
        tree.delete_one_node(tree.root())
        tree.tree_shape()
    #tree.render()
    raw_input()

