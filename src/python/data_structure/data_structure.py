#-*- coding: utf-8 -*-

class Node(object):
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
            raise RuntimeError("Invalid class %s is detected."\
                    %(str(other)))
        pass

    def __eq__(self, other):
        if isinstance(other, Node):
            return self._value == other._value
        else:
            raise RuntimeError("Invalid class %s is detected."\
                    %(str(other)))
        pass

    def __str__(self):
        if self._detail:
            return "(key:%s, value:%s)" % (str(self._key), str(self._value))
        else:
            return str(self._value)

    def _check_key(self):
        """(private) Check the validity of the key."""
        if not self._type == type(self._key):
            raise RuntimeError("Invalid type of key %s is detected."\
                    %(type(self._key)))
            return False
        return True

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
        pass

    def detail_on(self):
        self._detail = True
        pass

    def detail_off(self):
        self._detail = False

    pass

class Queue(object):
    """First In First Out (FIFO) data structure."""

    def __init__(self, value_list=[], priority_list=[]):
        """Create a Queue. Default priority is 419."""
        self._default_priority = 419
        self._queue = []
        if not type(value_list) in (list, tuple):
            raise RuntimeError("Invalid type of value list.")
        if not type(priority_list) in (list, tuple):
            raise RuntimeError("Invalid type of priority list.")
            
        if len(priority_list) == len(value_list):
            if len(priority_list) != 0:
                for i in xrange(len(value_list)):
                    self.push( value_list[i], priority_list[i] )
        else:
            if len(priority_list) != 0:
                raise RuntimeError("Invalid size of priority.")
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
            print e, ":", "Invalid priority is detected."
        except ValueError, e:
            print e, ":", "Invalid priority is detected."
            
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
        del self._default_priority
        del self._queue
        pass

    pass

class Stack(object):
    """Last In First Out (LIFO) data structure."""

    def __init__(self, *values):
        """Create a Stack."""
        self._stack = []
        if not type(values) in (list, tuple):
            raise RuntimeError("Invalid type of value list.")

        for val in values:
            if isinstance(val, list):
                for v in val:
                    self.push( v )
            else:
                self.push( val )
        pass

    def __del__(self):
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

class Element(object):
    """Element of linked list."""
    def __init__(self, value=None, before=None, after=None):
        if before!=None and not isinstance(before, Element):
            print before==None
            raise RuntimeError("Invalid class of variable before.")
        if after!=None and not isinstance(after, Element):
            raise RuntimeError("Invalid class of variable after.")
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
        if not isinstance(elem, Element):
            raise RuntimeError("Invalid class of variable elem.")
        self._next = elem
        pass

    def set_prev(self, elem=None):
        if not isinstance(elem, Element):
            raise RuntimeError("Invalid class of variable elem.")
        self._prev = elem
        pass

    def set_node(self, elem=None):
        if not isinstance(elem, Node):
            raise RuntimeError("Invalid class of variable elem.")
        self._node = elem
        pass

    def get_next(self):
        return self._next

    def get_prev(self):
        return self._prev

    def get_node(self):
        return self._node

    pass

class LinkedList(object):
    """Doubly linked list."""

    def __init__(self, *values):
        if not type(values) in (list, tuple):
            raise RuntimeError("Invalid type of value list.")

        self._head = Element()
        self._tail = Element( before=self._head )
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
        temp = Element( value )
        temp.set_prev( self._cursor.get_prev() )
        self._cursor.get_prev().set_next( temp )
        temp.set_next( self._cursor )
        self._cursor.set_prev( temp )
        self._size += 1
        pass

    def remove(self):
        if self._cursor == self._tail or self._cursor == self._head:
            raise RuntimeError("Invalid status of cursor.")

        prev = self._cursor.get_prev()
        self._cursor.get_prev().set_next( self._cursor.get_next() )
        self._cursor = self._cursor.get_next()
        temp = self._cursor.get_prev()
        del temp
        self._cursor.set_prev( prev )
        self._size -= 1
        pass

    def get_value(self):
        if self._cursor == self._tail or self._cursor == self._head:
            raise RuntimeError("Invalid status of cursor.")

        return self._cursor.get_node().get_value()

    def move_next(self):
        self._cursor = self._cursor.get_next()
        pass

    def move_prev(self):
        self._cursor = self._cursor.get_prev()
        pass

    def size(self):
        return self._size

    pass

class BinaryTree(object):
    pass

class BitMap(object):
    pass

# TEST
if __name__ == "__main__":
    data = [82,6309,96346,2,26,3,96,246,0,245,2,9,253,25]
    q = Queue(data)
    s = Stack(data)
    l = LinkedList(data)
    print "data: ", data
    print "Queue: ", q
    print "Stack: ", s
    print "Linked List: ", type(l), l, type(str(l))

    print 'size of queue', q.size()
    for i in xrange(q.size()):
        t = q.pop()
        print "Queue %d"%i, t
    print 'size of queue', q.size()
    del q

    print 'size of stack', s.size()
    for i in xrange(s.size()):
        t = s.pop()
        print "Stack %d"%i, t
    print 'size of stack', s.size()
    del s

    print 'size of linked list', l.size()
    for i in xrange(l.size()):
        t = l.get_value()
        l.remove()
        print "Linked List %d"%i, t
    print 'size of linked list', l.size()
    del l

    pass
