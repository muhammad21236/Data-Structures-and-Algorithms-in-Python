class MaxHeap:
    def __init__(self):
        self.heap = []

    def left_child(self, index):
        return index * 2 + 1

    def right_child(self, index):
        return index * 2 + 2

    def parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1
        while current > 0 and self.heap[current] > self.heap[self.parent(current)]:
            self._swap(current, self.parent(current))
            current = self.parent(current)

    def remove(self):
        if self.heap is None:
            return None

        if self.heap == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_value

    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self.left_child(index)
            right_index = self.right_child(index)

            if left_index < len(self.heap) and self.heap[left_index] > self.heap[index]:
                max_index = left_index
            if (
                right_index < len(self.heap)
                and self.heap[right_index] > self.heap[index]
            ):
                max_index = right_index

            if index != max_index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
