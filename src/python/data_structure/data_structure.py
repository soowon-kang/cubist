"""Useful data structures is implemented."""
#-*- coding: utf-8 -*-

class Node():
    """Node has key and value."""

    def __init__(self, value=None, key=0):
        """Create an Node. Defult key is 0."""
        self._value = value
        self._type = type(key)
        self._key = key
        self._detail = False
        pass

    def __cmp__(self, other):
        if isinstance(other, Node):
            return cmp(self._key, other._key)
        else:
            raise TypeError("Invalid class %s is detected."%(other))
        pass

    def __eq__(self, other):
        if isinstance(other, Node):
            return self._value == other._value
        else:
            raise TypeError("Invalid class %s is detected."%(other))
        pass

    def __str__(self):
        if self._detail:
            return "(key:%s, value:%s)" % (str(self._key), str(self._value))
        else:
            return str(self._value)

    def _check_key(self):
        """(private) Check the validity of the key."""
        if not isinstance(self._key, self._type):
            raise TypeError("Invalid type %s is detected."%(type(self._key)))

    def get_key(self):
        """Return the key of Node."""
        self._check_key()
        return self._key

    def get_value(self):
        """Return the value of Node."""
        self._check_key()
        return self._value
    
    def set_key(self, key):
        """Reset the key of Node."""
        self._key = key
        self._type = type(self._key)
        self._check_key()
        pass

    def set_value(self, value):
        """Reset the value of Node."""
        self._value = value
        pass

    def __del__(self):
        del self._type
        del self._key
        del self._value
        del self._detail
        pass

    def detail_on(self):
        self._detail = True
        pass

    def detail_off(self):
        self._detail = False

    pass

class Queue():
    """First In First Out (FIFO) data structure."""

    def __init__(self, value_list=[], priority_list=[]):
        """Create a Queue. Default priority is 419."""
        self._default_priority = 419
        self._queue = []
        p = priority_list
        if not (isinstance(value_list, list) or isinstance(value_list, tuple)):
            raise TypeError("Invalid type of value list.")
        if not isinstance(p, list) and not isinstance(p, tuple):
            raise TypeError("Invalid type of priority list.")
            
        if len(priority_list) == len(value_list):
            if len(priority_list) != 0:
                for i in xrange(len(value_list)):
                    self.push( value_list[i], priority_list[i] )
        else:
            if len(priority_list) != 0:
                raise ValueError("Invalid size of priority.")
            for value in value_list:
                self.push( value )
        pass
    
    def __str__(self):
        return ', '.join( map(str, self._queue) )

    def push(self, value, priority=None):
        """Push a Node into this queue. Default priority is 419."""
        if priority==None:
            priority = self._default_priority
        try:
            priority = int(priority)
        except TypeError, e:
            print e, ": Invalid type of variable priority."
        except ValueError, e:
            print e, ": Invalid value of variable priority."
            
        temp_node = Node(value=value, key=priority)
        # The nodes of queue need to describe detail informaiton.
        temp_node.detail_on()       
        self._queue.append( temp_node )
        pass

    def pop(self):
        """Return the first value of queue."""
        self._sort()
        return self._queue.pop(0).get_value()

    def size(self):
        """Return the size of queue."""
        return len( self._queue )

    def _sort(self):
        """(private) Sort this queue in order of priority."""
        self._queue.sort(reverse=True)
        pass

    def __del__(self):
        for _ in xrange( self._size ):
            self.pop()
        del self._queue
        del self._default_priority
        pass

    pass

class Stack():
    """Last In First Out (LIFO) data structure."""

    def __init__(self, *values):
        """Create a Stack."""
        self._stack = []
        if not isinstance(values, list) and not isinstance(values, tuple):
            raise TypeError("Invalid type of value list.")

        for val in values:
            if isinstance(val, list):
                for v in val:
                    self.push( v )
            else:
                self.push( val )
        pass

    def __del__(self):
        for _ in xrange( self._size ):
            self.pop()
        del self._stack
        pass

    def __str__(self):
        return ', '.join( map(str, self._stack) )

    def push(self, val):
        """Push a Node into this stack."""
        temp_node = Node( value=val )
        self._stack.append( temp_node )
        pass

    def pop(self):
        """Return the top value of stack, and remove it."""
        return self._stack.pop(-1).get_value()

    def get_top(self):
        """Return the top value of stack."""
        return self._stack[-1].get_value()

    def size(self):
        """Return the size of stack."""
        return len(self._stack)

    pass

class _ListElement():
    """(private)The element of linked list."""
    
    def __init__(self, value=None, before=None, after=None):
        """Create an element of linked list."""
        if before!=None and not isinstance(before, _ListElement):
            raise TypeError("Invalid class of variable before.")
        if after!=None and not isinstance(after, _ListElement):
            raise TypeError("Invalid class of variable after.")
        self._prev = before
        self._next = after
        self._node = Node( value )
        pass

    def __del__(self):
        self._prev.set_next( self._next )
        self._next.set_prev( self._prev )
        del self._node
        pass

    def set_next(self, elem=None):
        """Point the next element."""
        if not isinstance(elem, _ListElement):
            raise TypeError("Invalid class of variable elem.")
        self._next = elem
        pass

    def set_prev(self, elem=None):
        """Point the previous element."""
        if not isinstance(elem, _ListElement):
            raise TypeError("Invalid class of variable elem.")
        self._prev = elem
        pass

    def set_node(self, elem=None):
        """Store a node into current element."""
        if not isinstance(elem, Node):
            raise TypeError("Invalid class of variable elem.")
        self._node = elem
        pass

    def get_next(self):
        """Return the next element."""
        return self._next

    def get_prev(self):
        """Return the previous element."""
        return self._prev

    def get_node(self):
        """Return the saved node of current element."""
        return self._node

    pass

class LinkedList():
    """Doubly linked list."""

    def __init__(self, *values):
        """Create a Linked List."""
        if not isinstance(values, list) and not isinstance(values, tuple):
            raise TypeError("Invalid type of value list.")

        self._head = _ListElement()
        self._tail = _ListElement( before=self._head )
        self._head.set_next( self._tail )
        self._size = 0
        self._cursor = self._tail

        for val in values:
            if isinstance(val, list):
                for v in val:
                    self.add( v )
            else:
                self.add( val )

        self._cursor = self._head.get_next()
        pass

    def __del__(self):
        self._cursor = self._head.get_next()
        while not self._cursor == self._tail:
            self.remove()

        del self._head
        del self._tail
        del self._size
        del self._cursor
        pass

    def __str__(self):
        save_cursor = self._cursor
        self._cursor = self._head.get_next()
        temp = []
        while not self._cursor == self._tail:
            temp.append( str(self.get_value() ) )
            self.move_next()

        self._cursor = save_cursor
        return ', '.join( temp )

    def add(self, value):
        """Insert an element into the previous position of current cursor."""
        temp = _ListElement( value )
        temp.set_prev( self._cursor.get_prev() )
        self._cursor.get_prev().set_next( temp )
        temp.set_next( self._cursor )
        self._cursor.set_prev( temp )
        self._size += 1
        pass

    def remove(self):
        """Remove current element;
        also, make a link between the previous and the next elements."""
        if self._cursor == self._tail or self._cursor == self._head:
            raise IndexError("Invalid status of cursor.")

        prev = self._cursor.get_prev()
        self._cursor.get_prev().set_next( self._cursor.get_next() )
        self._cursor = self._cursor.get_next()
        temp = self._cursor.get_prev()
        del temp
        self._cursor.set_prev( prev )
        self._size -= 1
        pass

    def get_value(self):
        """Return the value of the node of current element."""
        if self._cursor == self._tail or self._cursor == self._head:
            raise IndexError("Invalid status of cursor.")

        return self._cursor.get_node().get_value()

    def move_next(self):
        """Move the cursor to the next element."""
        self._cursor = self._cursor.get_next()
        pass

    def move_prev(self):
        """Move the cursor to the previous element."""
        self._cursor = self._cursor.get_prev()
        pass

    def size(self):
        """Return the size of Linked List."""
        return self._size

    pass

class _TreeElement():
    """(private)The element of binary tree."""

    def __init__(self, value=None):
        self._parent = None
        self._left = None
        self._right = None
        self._node = Node( value )
        self._height = 1
        pass

    def __str__(self):
        return str( self._node.get_value() )

    def __del__(self):
        self._parent = None
        self._left = None
        self._right = None
        del self._node
        del self._height
        pass

    def __cmp__(self, other):
        if isinstance(other, _TreeElement):
            return cmp(self._node.get_value(), other._node.get_value())
        else:
            if other == None:
                return -1
            raise TypeError("Invalid class %s is detected."%(other))
        pass


    def _check_elem(self, elem=None):
        """(private)Check the validity of element."""
        if elem!=None and not isinstance(elem, _TreeElement):
            raise TypeError("Invalid class of variable elem.")

    def set_parent(self, elem=None):
        self._check_elem(elem)
        self._parent = elem
        pass

    def set_left(self, elem=None):
        self._check_elem(elem)
        self._left = elem
        pass

    def set_right(self, elem=None):
        self._check_elem(elem)
        self._right = elem
        pass

    def set_value(self, value=None):
        del self._node
        self._node = Node( value )
        pass

    def set_height(self, value=1):
        assert isinstance(value, int)
        self._height = value
        pass

    def get_parent(self):
        return self._parent

    def get_left(self):
        return self._left

    def get_right(self):
        return self._right

    def get_value(self):
        return self._node.get_value()

    def get_height(self):
        self._calc_height()
        return self._height

    def _calc_height(self):
        l = self.get_left()
        r = self.get_right()
        lh = 0
        if l:
            lh = l.get_height()
        rh = 0
        if r:
            rh = r.get_height()
        if lh < rh:
            self._height = rh+1
        else:
            self._height = lh+1


    def preorder(self):
        string = ""
        string += self.__str__()
        if isinstance(self._left, _TreeElement):
            string += " " + self._left.preorder()
        if isinstance(self._right, _TreeElement):
            string += " " + self._right.preorder()
        return string.strip()

    def inorder(self):
        string = ""
        if isinstance(self._left, _TreeElement):
            string += self._left.inorder()
        string += " " + self.__str__()
        if isinstance(self._right, _TreeElement):
            string += " " + self._right.inorder()
        return string.strip()

    def postorder(self):
        string = ""
        if isinstance(self._left, _TreeElement):
            string += self._left.postorder()
        if isinstance(self._right, _TreeElement):
            string += " " + self._right.postorder()
        string += " " + self.__str__()
        return string.strip()

    pass

class CompleteBinaryTree():
    """A complete binary tree is a binary tree in which every level,
    except possibly the last, is completely filled,
    and all nodes are as far left as possible.
    A tree is undirected acyclic connected graph."""
    
    def __init__(self, *values):
        """Create a complete binary tree."""
        if not isinstance(values, list) and not isinstance(values, tuple):
            raise TypeError("Invalid type of value list.")

        self._root = None
        self._size = 0

        for val in values:
            if isinstance(val, list):
                for v in val:
                    self.add( v )
            else:
                self.add( val )
        pass

    def __str__(self):
        return self.inorder_traversal()

    def __del__(self):
        for _ in xrange( self._size ):
            self.remove()
        del self._size
        del self._root
        pass

    def add(self, value):
        """Add a node into the last position."""
        self._size += 1
        num = bin(self._size)[3:]
        node = self._root
        v = _TreeElement( value )

        while len(num) > 1:
            if num[0] == '0':
                node = node.get_left()
            elif num[0] == '1':
                node = node.get_right()
            else:
                raise ValueError("Invalid State.")
            num = num[1:]

        if num == '':
            self._root = v
        elif num == '0':
            node.set_left( v )
            v.set_parent( node )
        elif num == '1':
            node.set_right( v )
            v.set_parent( node )
        else:
            raise ValueError("Invalid State.")

        pass

    def remove(self):
        """Remove a node of the last position."""
        num = bin(self._size)[3:]
        node = self._root

        while len(num) > 1:
            if num[0] == '0':
                node = node.get_left()
            elif num[0] == '1':
                node = node.get_right()
            else:
                raise ValueError("Invalid State.")
            num = num[1:]

        if num == '':
            del node
            self._root = None
        else:
            parent = node
            if num == '0':
                node = node.get_left()
                parent.set_left( None )
            elif num == '1':
                node = node.get_right()
                parent.set_right( None )
            else:
                raise ValueError("Invalid State.")
            del node

        self._size -= 1
        pass

    def preorder_traversal(self):
        return self._root.preorder()

    def inorder_traversal(self):
        return self._root.inorder()

    def postorder_traversal(self):
        return self._root.postorder()

    def size(self):
        return self._size

    pass

# TODO
class AVLTree():
    "Adelson-Velsky & Landis'62: self-balancign binary search tree.\
    Heights of any two sibling subtrees must differ by at most one."

    def __init__(self, *values):
        """Create a AVL tree."""
        if not isinstance(values, list) and not isinstance(values, tuple):
            raise TypeError("Invalid type of value list.")

        self._root = None
        self._size = 0

        for val in values:
            if isinstance(val, list):
                for v in val:
                    self.add( v )
            else:
                self.add( val )
        pass

    def __str__(self):
        return self.preorder_traversal()
    
    def __del__(self):
        del self._root
        del self._size
        pass

    def add(self, value=None):
        """Add a node with avl condition."""
        self._size += 1
        if self._root == None:
            self._root = _TreeElement( value )
            return
        cursor = self._root
        while True:
            if not isinstance(value, type(cursor.get_value())):
                raise TypeError("Invalid type of value.")
            if cursor.get_value() < value:
                if cursor.get_right() == None:
                    v = _TreeElement(value)
                    v.set_parent( cursor )
                    cursor.set_right( v )
                    self._balancing( v )
                    return
                else:
                    cursor = cursor.get_right()
            else:
                if cursor.get_left() == None:
                    v = _TreeElement(value)
                    v.set_parent( cursor )
                    cursor.set_left( v )
                    self._balancing( v )
                    return
                else:
                    cursor = cursor.get_left()
        pass

    def remove(self, value=None):
        """Remove a node which value is same as argument."""
        elem = self._root
        while elem != None:
            v = elem.get_value()
            if v < value:
                elem = elem.get_right()
            elif value < v:
                elem = elem.get_left()
            elif v == value:
                # type check is needed
                break
            else:
                raise ValueError('Invalid value.')
        if elem != None:
            self._size -= 1
            parent = elem.get_parent()
            leftmost = elem.get_right()
            l = elem.get_left()
            while leftmost != None and leftmost.get_left() != None:
                leftmost = leftmost.get_left()
            if leftmost != None:
                if parent != None:
                    if parent.get_value() < value:
                        parent.set_right( leftmost )
                    else:
                        parent.set_left( leftmost )
                else:
                    self._root = leftmost
                lp = leftmost.get_parent()
                if lp != elem:
                    lr = leftmost.get_right()
                    lp.set_left( lr )
                    if lr != None:
                        lr.set_parent( lp )
                    er = elem.get_right()
                    leftmost.set_right( er )
                    er.set_parent( leftmost )

                leftmost.set_parent( parent )
                leftmost.set_left( l )
                if l != None:
                    l.set_parent( leftmost )
            else:
                if parent != None:
                    if parent.get_value() < value:
                        parent.set_right( l )
                    else:
                        parent.set_left( l )
                else:
                    self._root = l
                if l != None:
                    l.set_parent( parent )

            elem.set_parent( None )
            elem.set_left( None )
            elem.set_right( None )
            if parent != None:
                pr = parent.get_right()
                pl = parent.get_left()
                if pl != None:
                    pll = pl.get_left()
                    plr = pl.get_right()
                    if pll != None:
                        self._balancing( pll )
                    if plr != None:
                        self._balancing( plr )
                if pr != None:
                    prr = pr.get_right()
                    prl = pr.get_left()
                    if prl != None:
                        self._balancing( prl )
                    if prr != None:
                        self._balancing( prr )
        else:
            raise ValueError('There is no such element.')
        pass

    def _calc_height(self):
        self._root.get_height()

    def _balancing(self, elem=None):
        """(private) Check and reconstruct the avl condition."""
        if not isinstance(elem, _TreeElement):
            raise TypeError("Invalid type of value.")
        self._calc_height()
        parent = elem.get_parent()
        saved_elem = elem

        while parent != None:
            r = parent.get_right()
            l = parent.get_left()
            avl = 0
            if r != None:
                avl += r.get_height()
            if l != None:
                avl -= l.get_height()

            if -1 <= avl <= 1:
                saved_elem = elem
                elem = parent
                parent = elem.get_parent()
            else:
                # need to balance
                p = parent.get_parent()
                x = parent.get_value()
                y = elem.get_value()
                z = saved_elem.get_value()
                mid = elem
                if z <= y:
                    if y <= x:
                        mid = elem
                        r = elem.get_right()
                        parent.set_left( r )
                        if r != None:
                            r.set_parent( parent )
                        #elem.set_left( saved_elem )
                        elem.set_right( parent )
                        #saved_elem.set_parent( elem )
                        parent.set_parent( elem )
                        temp = parent.get_right()
                    else:
                        mid = saved_elem
                        l = saved_elem.get_left()
                        r = saved_elem.get_right()
                        parent.set_right( l )
                        if l != None:
                            l.set_parent( parent )
                        elem.set_left( r )
                        if r != None:
                            r.set_parent( elem )
                        saved_elem.set_left( parent )
                        saved_elem.set_right( elem )
                        parent.set_parent( saved_elem )
                        elem.set_parent( saved_elem )
                        temp = parent.get_left()
                else:
                    if y <= x:
                        mid = saved_elem
                        l = saved_elem.get_left()
                        r = saved_elem.get_right()
                        parent.set_left( r )
                        if r != None:
                            r.set_parent( parent )
                        elem.set_right( l )
                        if l != None:
                            l.set_parent( elem )
                        saved_elem.set_left( elem )
                        saved_elem.set_right( parent )
                        elem.set_parent( saved_elem )
                        parent.set_parent( saved_elem )
                        temp = parent.get_right()
                    else:
                        mid = elem
                        l = elem.get_left()
                        parent.set_right( l )
                        if l != None:
                            l.set_parent( parent )
                        elem.set_left( parent )
                        #elem.set_right( saved_elem )
                        parent.set_parent( elem )
                        #saved_elem.set_parent( elem )
                
                mid.set_parent( p )
                if p != None:
                    if mid.get_value() <= p.get_value():
                        p.set_left( mid )
                    else:
                        p.set_right( mid )
                else:
                    self._root = mid
                break
        pass

    def preorder_traversal(self):
        return self._root.preorder()

    def inorder_traversal(self):
        return self._root.inorder()

    def postorder_traversal(self):
        return self._root.postorder()

    def size(self):
        return self._size

    pass

class BitMap():
    pass

# TEST
if __name__ == "__main__":
    data = [82,6309,96346,2,26,3,96,246,0,245,2,9,253,25]
    print "data: ", data

    q = Queue(data)
    print "Queue: ", q
    print 'size of queue', q.size()
    for i in xrange(q.size()):
        t = q.pop()
        print "Queue %d"%i, t
    print 'size of queue', q.size()
    del q

    s = Stack(data)
    print "Stack: ", s
    print 'size of stack', s.size()
    for i in xrange(s.size()):
        t = s.pop()
        print "Stack %d"%i, t
    print 'size of stack', s.size()
    del s
    
    l = LinkedList(data)
    print "Linked List: ", type(l), l, type(str(l))
    print 'size of linked list', l.size()
    for i in xrange(l.size()):
        t = l.get_value()
        l.remove()
        print "Linked List %d"%i, t
    print 'size of linked list', l.size()
    del l
    
    b = CompleteBinaryTree(data)
    print "Binary Tree: ", b
    for i in xrange(b.size()):
        print 'size of binary tree', b.size()
        print b.preorder_traversal()
        print b.inorder_traversal()
        print b.postorder_traversal()
        b.remove()
        #t = b.get_value()   #wrong
    print 'size of binary tree', b.size()
    del b

    print 'An example of binary tree construction.'
    j = _TreeElement( 'J' )
    w = _TreeElement( 'W' )
    z = _TreeElement( 'Z' )
    r = _TreeElement( 'R' )
    l = _TreeElement( 'L' )
    e = _TreeElement( 'E' )
    h = _TreeElement( 'H' )
    c = _TreeElement( 'C' )
    x = _TreeElement( 'X' )
    k = _TreeElement( 'K' )
    y = _TreeElement( 'Y' )
    s = _TreeElement( 'S' )
    q = _TreeElement( 'Q' )
    t = _TreeElement( 'T' )
    a = _TreeElement( 'A' )
    b = _TreeElement( 'B' )
    p = _TreeElement( 'P' )
    d = _TreeElement( 'D' )
    f = _TreeElement( 'F' )
    m = _TreeElement( 'M' )
    n = _TreeElement( 'N' )
    u = _TreeElement( 'U' )
    g = _TreeElement( 'G' )
    z.set_left( j )
    z.set_right( w )
    l.set_left( z )
    l.set_right( r )
    e.set_left( h )
    e.set_right( l )
    x.set_left( e )
    x.set_right( c )
    k.set_left( x )
    t.set_left( s )
    t.set_right( q )
    y.set_right( a )
    y.set_left( t )
    k.set_right( y )
    n.set_left( u )
    n.set_right( g )
    f.set_left( m )
    f.set_right( n )
    p.set_left( d )
    p.set_right( f )
    b.set_left( k )
    b.set_right( p )
    
    print 'preorder :', b.preorder()
    print 'postorder :', b.postorder()
    print 'inorder :', b.inorder()

    del a,b,c,d,e,f,g,h,j,k,l,m,n,p,q,r,s,t,u,w,x,y,z

    avl = AVLTree(data)
    print "AVLTree: ", avl

    for t in data:
        print 'size of avl tree', avl.size()
        print 'pre ', avl.preorder_traversal()
        print 'in  ', avl.inorder_traversal()
        print 'post', avl.postorder_traversal()
        avl.remove( t )
        print 'remove', t
    print 'size of avl tree', avl.size()
    del avl

    pass
