class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency


class MinHeap:
    def __init__(self):
        self.data = []

    def heapify_up(self, index):
        # Swap with the parent until the parent's urgency is no longer higher
        while index > 0:
            parent = (index - 1) // 2
            if self.data[index].urgency >= self.data[parent].urgency:
                break
            self.data[index], self.data[parent] = self.data[parent], self.data[index]
            index = parent

    def heapify_down(self, index):
        # Swap with the smaller child until neither child has a lower urgency
        size = len(self.data)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left
            if right < size and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right

            if smallest == index:
                break
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            index = smallest

    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def print_heap(self):
        print("Current Queue:")
        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")

    def peek(self):
        if not self.data:
            return None
        return self.data[0]

    def remove_min(self):
        if not self.data:
            return None

        # Move the last patient to the root, then restore the heap property
        root = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            self.heapify_down(0)
        return root


# Test your MinHeap class here including edge cases
if __name__ == "__main__":
    p1 = Patient("Riley", 2)
    print(p1.name)     # Riley
    print(p1.urgency)  # 2

    heap = MinHeap()
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))
    heap.print_heap()
    # Current Queue:
    # - Taylor (1)
    # - Jordan (3)
    # - Avery (5)

    next_up = heap.peek()
    print(next_up.name, next_up.urgency)  # Taylor 1

    served = heap.remove_min()
    print(served.name)  # Taylor
    heap.print_heap()
    # Current Queue:
    # - Jordan (3)
    # - Avery (5)

    # Edge cases: an empty heap returns None instead of crashing
    empty = MinHeap()
    print(empty.peek())        # None
    print(empty.remove_min())  # None
    empty.print_heap()         # Current Queue:

    # Edge case: removing the only patient leaves the heap empty
    single = MinHeap()
    single.insert(Patient("Sam", 4))
    print(single.remove_min().name)  # Sam
    print(single.data)               # []

    # Edge case: patients come out in urgency order, including ties
    busy = MinHeap()
    for name, urgency in [("A", 7), ("B", 2), ("C", 9), ("D", 2), ("E", 1), ("F", 10)]:
        busy.insert(Patient(name, urgency))
    order = []
    while busy.peek() is not None:
        order.append(busy.remove_min().urgency)
    print(order)  # [1, 2, 2, 7, 9, 10]
