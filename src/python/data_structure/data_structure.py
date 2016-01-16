#-*- coding: utf-8 -*-

class Node(object):
    """Node has key and value."""

    def __init__(self, value=None, key=0):
        """Create an Node. Defult key is 0."""
        self._value = value
        self._type = type(key)
        self._key = key
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
        return "key: %s, value: %s" % (str(self._key), str(self._value))

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
        return str( map(str, self._queue) )

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

    def __init__(self, value_list=[]):
        """Create a Stack."""
        self._stack = []
        if not type(value_list) in (list, tuple):
            raise RuntimeError("Invalid type of value list.")

        for value in value_list:
            self.push( value=value )
        pass

    def __del__(self):
        del self._stack
        pass

    def __str__(self):
        return str( map(str, self._stack) )

    def push(self, value):
        """Push a Node into this stack."""
        temp_node = Node( value=value )
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
    def __init__(self, value=None, prev_=None, next_=None):
        if not isinstance(prev_, Element):
            raise RuntimeError("Invalid class of variable prev_.")
        if not isinstance(next_, Element):
            raise RuntimeError("Invalid class of variable next_.")
        self._prev = prev_
        self._next = next_
        self._curr = Node( value=value )
        pass

    def __del__(self):
        self._prev.set_next( self._next )
        self._next.set_prev( self._prev )
        del self._curr
        pass

    def set_next(self, elem=None):
        pass

    def set_prev(self, elem=None):
        pass

    def set_curr(self, elem=None):
        pass

    def get_next(self):
        pass

    def get_prev(self):
        pass

    pass

class LinkedList(object):
    """Doubly linked list."""

    def __init__(self, value_list=[]):
        pass

    def __del__(self, value_list=[]):
        pass

    def __str__(self, value_list=[]):
        pass

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
    print "data: ", data
    print "Queue: ", q
    print "Stack: ", s
    for i in xrange(q.size()):
        t = q.pop()
        print "Queue %d"%i, t
    for i in xrange(s.size()):
        t = s.pop()
        print "Stack %d"%i, t

    pass

'''
class LinkedList(object):
    """Doubly linked list."""

    def __init__(self, value_list=[]):
        self._list = []
        self._index = -1    # need to debug
        if not type(value_list) in (list, tuple):
            raise RuntimeError("Invalid type of value list.")

        for value in value_list:
            _check_value( val=value )
            self.push_back( value=value )

    def __del__(self):
        del self._list
        del self._index
        pass

    def __str__(self):
        pass

    def push_front(self, value=None):
        _check_value( val=value )
        self._list = [ value ]+self._list
        pass

    def push_back(self, value=None):
        _check_value( val=value )
        self._list = self._list+[ value ]
        pass

    def insert_front(self, value=None):
        _check_value( val=value )
        pass

    def insert_back(self, value=None):
        _check_value( val=value )
        pass

    def pop_front(self):
        return self._list.pop(0).get_value()

    def pop_back(self):
        return self._list.pop(-1).get_value()

    def get_current_node(self):
        return self._list[self._index].get_value()

    def get_pre_node(self):
        return self._list[self._index-1].get_value()

    def get_post_node(self):
        return self._list[self._index+1].get_value()

    def get_head(self):
        return self._list[0].get_value()

    def get_tail(self):
        return self._list[-1].get_value()

    def size(self):
        return len(self._list)

    def _check_value(self, val=None):
        """(private) Check the validity of the input value."""
        if val == None:
            raise RuntimeError("Invalid value %s is detected."\
                    %(type(val)))
            return False
        return True

    pass
'''
