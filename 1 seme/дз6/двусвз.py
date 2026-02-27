class Node:
    def __init__(self, val=None):
        self.prev = None
        self.val = val
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def append(self, new):
        new_node = Node(new)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.len += 1

    def get(self, index):
        if index < self.len:
            cur = self.head
            for i in range(index):
                cur = cur.next
            return cur.val
        print('Oshibka')

    # def remove(self, val):
    #     cur = self.head
    #     if cur:
    #         if cur.val == val:
    #             self.head = cur.next
    #             self.len -=1
    #             return
    #         while val != cur.next.val or cur.next:
    #             cur = cur.next
    #         if cur is None:
    #             print('Niet')
    #             return
    #         cur.next= cur.next.next
    #         self.len -=1

    def remove(self, index):
        if index < 0 or index >= self.len or self.head is None:
            print('Oshibka')
            return

        cur = self.head
        for i in range(index):
            cur = cur.next

        # -голова
        if cur == self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None

        # rip хвост
        elif cur == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None

        # mid
        else:
            cur.prev.next = cur.next
            cur.next.prev = cur.prev

        self.len -= 1

        print('oshibka')

    def __len__(self):
        return self.len

    def __contains__(self, val):
        cur = self.head
        while(cur):
            if cur.val == val:
                return True
            else:
                cur = cur.next
        return False


