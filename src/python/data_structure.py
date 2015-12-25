#-*- coding: utf-8 -*-

class Node(object):
    """Node has key and value."""

    def __init__(self, value=None, key=0):
        """Create an Node. Defult key is 0."""
        self._value = value
        self._type = type(key)
        self._key = key

    def __cmp__(self, other):
        if isinstance(other, Node):
            return cmp(self._key, other._key)
        else:
            raise RuntimeError("Invalid class %s is detected."\
                    %(str(other)))

    def __eq__(self, other):
        if isinstance(other, Node):
            return self._value == other._value
        else:
            raise RuntimeError("Invalid class %s is detected."\
                    %(str(other)))

    def __str__(self):
        return "key: %s, value: %s" % (str(key), str(value))

    def _check_key(self):
        """(private) Check the initial type of key."""
        if not self._type == type(self._key):
            raise RuntimeError("Invalid type of key %s is detected."\
                    %(type(key)))
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

    def set_value(self, value):
        """Reset the value of Node."""
        self._value = value

    def __del__(self):
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
    
    def __str__(self):
        return str( map(str, self._queue) )

    def push(self, value, priority=None):
        """Push a Node to this queue. Default priority is 419."""
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

    def pop(self):
        """Return first value."""
        self._sort()
        return self._queue.pop(0).get_value()

    def size(self):
        """Return the size of this queue."""
        return len( self._queue )

    def _sort(self):
        """(private) Sort this queue in order of priority."""
        self._queue.sort(reverse=True)

    def __del__(self):
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

    def __del__(self):
        pass

    def __str__(self):
        return str( map(str, self._stack) )

    def push(self, value):
        temp_node = Node( value=value )
        self._stack.append( temp_node )

    def pop(self):
        return self._stack.pop(-1).get_value()

    def size(self):
        return len(self._stack)

class LinkedList(object):
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
    print "Queue: ", q
    print "Stack: ", s
    for i in xrange(q.size()):
        print "Queue %d"%i, q.pop()
        print "Stack %d"%i, s.pop()

    pass

