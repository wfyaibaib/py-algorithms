import sys
import rbtree
from PySide.QtGui import *
from PySide.QtCore import *
class BaseNode:
    pass
class BaseLink:
    pass

def rbtree_node_depth_adjust(tree):
    if tree.empty():
        return
    def traverse(subtree, red_cnt):
        if subtree is tree.head:
            return
        if subtree.color is False:
            red_cnt += 1
        subtree.depth -= red_cnt
        traverse(subtree.l, red_cnt)
        traverse(subtree.r, red_cnt)

    traverse(tree.root(), 0)

def create_node_cnt_for_tree(subtree, head):
    if subtree is head:
        subtree.cnt = 0
        return 0
    else:
        l_cnt = create_node_cnt_for_tree(subtree.l, head)
        r_cnt = create_node_cnt_for_tree(subtree.r, head)
        subtree.cnt = l_cnt + r_cnt + 1
        return subtree.cnt
def create_node_depth_for_tree(subtree, init_value,  head):
    if subtree is head:
        return
    subtree.depth = init_value
    create_node_depth_for_tree(subtree.l, init_value + 1, head)
    create_node_depth_for_tree(subtree.r, init_value + 1, head)

def create_x_pos_for_tree(tree):
    if tree.empty():
        return
    cnt = 0
    for node in tree:
        node.x = cnt
        cnt += 1

def get_x_y_for_node(node, head):
    x = node.x
    y = node.depth
    return (x, y)

app = QApplication(sys.argv)
class BaseScene(QGraphicsScene):
    def add_item_from_tree(self, tree):
        if tree.empty():
            return
        head = tree.head


        def create_all_nodes(subtree):
            if subtree is head:
                return
            subtree.item = BaseNode()
            subtree.item.node = subtree
            subtree.item.setToolTip(str(subtree.data))
            self.addItem(subtree.item)
            create_all_nodes(subtree.l)
            create_all_nodes(subtree.r)

        create_all_nodes(tree.root())

        def create_all_links(subtree):
            if subtree is head:
                return
            if subtree.l is not head:
                link = BaseLink(subtree.item, subtree.l.item)
                self.addItem(link)
                # print 'l add'
            if subtree.r is not head:
                link = BaseLink(subtree.item, subtree.r.item)
                self.addItem(link)
                # print 'r add'
            create_all_links(subtree.l)
            create_all_links(subtree.r)


        #pos
        #create_node_cnt_for_tree(tree.root(), tree.head)
        create_node_depth_for_tree(tree.root(), 0, tree.head)
        rbtree_node_depth_adjust(tree)
        create_x_pos_for_tree(tree)

        create_all_links(tree.root())

        for node in tree:
            # node.item.prepareGeometryChange()
            node.item.setPos(node.x * 30, node.depth * 30)

        create_all_links(tree.root())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F5:
            pass

class BaseView(QGraphicsView):
    def __init__(self):
        QGraphicsView.__init__(self)
        self.setDragMode(QGraphicsView.RubberBandDrag)
        self.setRenderHint(QPainter.Antialiasing)

    def wheelEvent(self, event):
        if event.delta() > 0:
            self.scale(1.1, 1.1)
        else:
            self.scale(0.9, 0.9)

class BaseNode(QGraphicsItem):
    def __init__(self, *args, **kwargs):
        QGraphicsItem.__init__(self, *args, **kwargs)
        # self.setZValue()
        self.links = []
        self.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemSendsGeometryChanges)

    def add_link(self, link):
        self.links.append(link)

    def remove_link(self, link):
        self.links.remove(link)

    def setPos(self, *args, **kwargs):
        QGraphicsItem.setPos(self, *args, **kwargs)
        for l in self.links:
            l.trackNodes()

    def boundingRect(self):
        penWidth = 1.0
        return QRectF(-10 - penWidth / 2, -10 - penWidth / 2,
                      20 + penWidth, 20 + penWidth)

    def itemChange(self, change, value):
        # print 'changed', change
        if change == QGraphicsItem.ItemPositionChange :
            # print self.data
            for l in self.links:
                # print 'call track'
                l.trackNodes()
            # value is the new position.
        return QGraphicsItem.itemChange(self, change, value)

    def paint(self, painter, option, widget):
        #painter.drawRoundedRect(-10, -10, 20, 20, 5, 5)
        painter.setBrush(Qt.red if self.node.color is False else Qt.black)
        painter.drawEllipse(-10, -10, 20, 20)

        painter.setPen(Qt.white)
        painter.drawText(self.boundingRect(), Qt.AlignCenter, str(self.node.data))

        #self.setZValue(-1)

    def __del__(self):
        for l in self.links:
            del l

class BaseLink(QGraphicsLineItem):
    def __init__(self, start, end, *args, **kwargs):
        QGraphicsLineItem.__init__(self)
        self.start = start
        self.end = end

        self.start.add_link(self)
        self.end.add_link(self)

        #self.setFlags(QGraphicsItem.ItemIsSelectable);
        self.setZValue(-1);

        self.setPen(QPen(QColor(Qt.blue), 1.0) )
        self.trackNodes()

    def trackNodes(self):
        self.setLine(QLineF(self.start.pos(), self.end.pos()))

    def __del__(self):
        self.start.remove_link(self)
        self.end.remove_link(self)


view = BaseView()
scene = BaseScene()
view.setScene(scene)
view.show()

tree = rbtree.Rbtree()
tree.insert_data_list(range(20))
tree.tree_shape()
scene.add_item_from_tree(tree)
scene.setBackgroundBrush(Qt.white)
view.setBackgroundBrush(Qt.white)
rect = scene.itemsBoundingRect()
img = QImage(rect.width(), rect.height(), QImage.Format_RGB32)
p = QPainter(img)
scene.render(p)
p.end()
print scene.sceneRect()
img.save('scene.png')


# tree.root().item.setPos(0, 400)
# for node in tree:
#     print node.data, node.x, node.depth

# node1 = BaseNode()
# node1.setPos(0, 0)
#
# node2 = BaseNode()
# node2.setPos(100, 200)
#
# scene.addItem(node1)
# scene.addItem(node2)
#
# link = BaseLink(node1, node2)
# scene.addItem(link)
# #link.setZValue(1)
#
# print node1.zValue(), node2.zValue(), link.zValue()
# node1 = QGraphicsEllipseItem(0, 0, 100, 400)
# #node1.setFlags(QGraphicsItem.ItemIsSelectable)
# node1.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemSendsGeometryChanges)
# node2 = QGraphicsEllipseItem(0, 0, 100, 400)
# node2.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemSendsGeometryChanges)
# scene.addItem(node1)
# scene.addItem(node2)
# scene.addEllipse(0, 0, 100, 400)
# scene.addEllipse(0, 0, 100, 400)
# scene.addEllipse(0, 0, 100, 400)
app.exec_()
#sys.exit()