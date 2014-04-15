class Node():
    unique_name = 0
    def __init__(self, data = None, left = None, right = None, parent = None):
        self.data = data
        self.l= left
        self.r = right
        self.p = parent

        Node.unique_name += 1
        self.name = str(Node.unique_name)
        self.label = str(self.data)

    def __str__(self):
        return str(self.data)

    def copy_data_from(self, other):
        self.data = other.data



def left(node):
    return node.l

def right(node):
    return node.r

def parent(node):
    return node.p

def bst_left_most(root, head = None):
    c = root.l
    while c is not head:
        root = c
        c = root.l
    return root

def bst_right_most(root, head = None):
    c = root._r
    while c is not head:
        root = c
        c = root._r
    return root

def uncle(node):
    p = parent(pnode)
    pp = parent(p)
    if (left(pp) == p):
        return right(pp)
    else:
        return left(pp)

def sibling(node):
    p = parent(node)
    if (left(p) == node):
        return right(p)
    else:
        return left(p)

def bst_left_rotation(node, head):
    p = parent(node)
    r = right(node)
    rl = left(r)

    node.r = rl
    if rl is not head:
        rl.p = node

    r.l = node
    node.p = r

    r.p = p
    if p is head:
        if p is None:
            return
        else:
            p.p = r
    elif node is left(p):
        p.l = r
    else:
        p.r = r

def bst_right_rotation(node, head):
    p = parent(node)
    l = left(node)
    lr = right(r)

    node.l = lr
    if lr is not head:
        lr.p = node

    l.r = node
    node.p = l

    l.p = p
    if p is head:
        if p is None:
            return
        else:
            p.p = l
    elif node is left(p):
        p.l = l
    else:
        p.r = l
def bst_find_insert_position(root, inserted, head, cmp_key):
    p = root
    c = root
    while c is not head:
        p = c
        if cmp_key(inserted, p):
            c = left(p)
        else:
            c = right(p)
    return p

def bst_successor(node, head):
    if right(node) is not head:
        return bst_left_most(right(node), head)
    else:
        c = node
        p = parent(c)
        while p is not Node and c is right(p):
            c = p
            p = parent(p)
        return p

def bst_predecessor(node, head):
    if left(node) is not head:
        return bst_right_most(right(node), head)
    else:
        c = node
        p = parent(c)
        while p is not Node and c is left(p):
            c = p
            p = parent(p)
        return p

def bst_is_root(node, head = None):
    return parent(node) is head

def bst_insert_one_node(root, head, inserted, cmp_key, unique):
    p = bst_find_insert_position(root, head, inserted, cmp_key)
    if p is head:
        if head is not None:
            head.p = inserted
        inserted.p = head
        return inserted
    else:
        if unique and not cmp_key(inserted, p) and not cmp_key(p, inserted):
            return None
        else:
            inserted.p = p
            if (cmp_key(inserted, p)):
                p.l = inserted
            else:
                p.r = inserted
            return inserted

def bst_delete_one_node(delete, head):
    d = delete
    if left(delete) is not head and right(delete) is not head:
        d = bst_successor(delete, head)
        delete.copy_data_from(d)
    n = left(d) if head is right(d) else right(d)
    p = parent(d)
    if p is head:
        if head is None:
            if n is not None:
                n.p = None
            else:
                head.p = n
                if n is not head:
                    n.p = p
    else:
        if d is left(p):
            p.l = n
        else:
            p.r = n
        if n is not head:
            n.p = p
    del d

if __name__ == '__main__':
    a  = Node(data = 1)
    b = Node(data = 2, left = a)
    print b


