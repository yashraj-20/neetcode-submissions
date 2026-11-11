class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_front(self, node):
        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def remove_last(self):
        if self.tail.prev is self.head:
            return None
        node = self.tail.prev
        self.remove(node)
        return node

class LRUCache:
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.list = DoublyLinkedList()

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache.get(key)
        self.list.remove(node)
        self.list.add_front(node)
        return node.val


    def put(self, key, val):
        if self.capacity == 0:
            return None

        if key in self.cache:
            old_node = self.cache.get(key)
            old_node.val = val
            self.list.remove(old_node)
            self.list.add_front(old_node)
        else:
            node = Node(key, val)
            if len(self.cache) == self.capacity:
                old_node = self.list.remove_last()
                del self.cache[old_node.key]
                self.list.add_front(node)
                self.cache[key] = node
            else:
                self.list.add_front(node)
                self.cache[key] = node
