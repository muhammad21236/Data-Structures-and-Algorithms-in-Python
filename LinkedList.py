class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        new_node = Node(data)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            self.head = new_node
            self.head.next = temp
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.data

    def pop_first(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 0

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, data):
        if index < 0 or index >= self.length:
            return None
        temp = self.get(index)
        if temp:
            temp.data = data
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False

        if index == 0:
            self.prepend(value)
        if index == 1:
            self.append(value)

        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 and index > self.length:
            return None

        if index == 0:
            return self.pop_first()

        if index == self.length:
            return self.pop()

        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def middle_node(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def remove_duplicates(self):
        current = self.head
        seen = set()
        while current:
            if current.data in seen:
                self.remove(current.data)
            else:
                seen.add(current.data)
            current = current.next

    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def find_cycle_start(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return None
        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

    def find_cycle_length(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return 0
        length = 1
        current = slow.next
        while current != slow:
            length += 1
            current = current.next
        return length

    def remove_cycle(self):
        cycle_start = self.find_cycle_start()
        if not cycle_start:
            return
        current = cycle_start
        while current.next != cycle_start:
            current = current.next
        current.next = None

    def is_palindrome(self):
        slow = self.head
        fast = self.head
        stack = []
        while fast and fast.next:
            stack.append(slow.data)
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        while slow:
            if stack.pop() != slow.data:
                return False
            slow = slow.next
        return True

    def kth_to_last(self, k):
        if k < 1 or k > self.length:
            return None
        slow = self.head
        fast = self.head
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow

    def kth_to_last_recursive(self, k):
        def helper(node):
            if node is None:
                return 0
            count = helper(node.next) + 1
            if count == k:
                self.kth_node = node
            return count

        self.kth_node = None
        helper(self.head)
        return self.kth_node

    def kth_to_last_iterative(self, k):
        if k < 1 or k > self.length:
            return None
        slow = self.head
        fast = self.head
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow

    def kth_to_last_two_pointers(self, k):
        if k < 1 or k > self.length:
            return None
        slow = self.head
        fast = self.head
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow

    def kth_to_last_one_pointer(self, k):
        if k < 1 or k > self.length:
            return None
        slow = self.head
        fast = self.head
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow

    def kth_to_last_two_pointers_optimized(self, k):
        if k < 1 or k > self.length:
            return None
        slow = self.head
        fast = self.head
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow

    def kth_to_last_one_pointer_optimized(self, k):
        if k < 1 or k > self.length:
            return None
        slow = self.head
        fast = self.head
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow

    def kth_to_last_two_pointers_recursive(self, k):
        if k < 1 or k > self.length:
            return None
        slow = self.head
        fast = self.head
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow

    def kth_to_last_one_pointer_recursive(self, k):
        if k < 1 or k > self.length:
            return None
        slow = self.head
        fast = self.head
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow

    def kth_to_last_two_pointers_iterative(self, k):
        if k < 1 or k > self.length:
            return None
        slow = self.head
        fast = self.head
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow

    def kth_to_last_one_pointer_iterative(self, k):
        if k < 1 or k > self.length:
            return None
        slow = self.head
        fast = self.head
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow

    def kth_to_last_two_pointers_optimized_iterative(self, k):
        if k < 1 or k > self.length:
            return None
        slow = self.head
        fast = self.head
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow

    def kth_to_last_one_pointer_optimized_iterative(self, k):
        if k < 1 or k > self.length:
            return None
        slow = self.head
        fast = self.head
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow


def find_kth_node_end(ll, k):
    slow = fast = ll.head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    return slow


def find_kth_node_start(ll, k):
    slow = ll.head
    for _ in range(k - 1):
        if slow is None:
            return None
        slow = slow.next
    return slow


my_linked_list = LinkedList(5)

my_linked_list.append(2)
my_linked_list.append(8)
my_linked_list.append(3)
my_linked_list.append(5)
# my_linked_list.print_list()
my_linked_list.remove(4)
my_linked_list.print_list()
