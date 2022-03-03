class Heap:

    def __init__(self):
        self.data = []

    def root_node(self):
        return self.data[0]

    def last_node(self):
        return self.data[-1]

    def left_child_index(self, index):
        return (index * 2) + 1

    def right_child_index(self, index):
        return (index * 2) + 2

    def parent_index(self, index):
        return (index - 1) // 2

    def insert(self, value):
        # Turn value into last node by inserting it at the end of the array
        self.data.append(value)

        # Keep track of the index of the newly inserted node
        new_node_index = len(self.data) - 1

        # The following loop executes the "Trickle up" algorithm

        # If the new node is not in the root position,
        # and it's greater than its parent node:
        while new_node_index > 0 and self.data[new_node_index] > self.data[self.parent_index(new_node_index)]:
            self.data[self.parent_index(new_node_index)], self.data[new_node_index] = \
                self.data[new_node_index], self.data[self.parent_index(new_node_index)]

            new_node_index = self.parent_index(new_node_index)

    def delete(self):
        # We only ever delete the root node from a heap, so we
        # pop the last node from the array and make it the root node
        value = self.data[0]
        self.data[0] = self.data.pop()

        # Track the current index of the "Trickle node"
        trickle_node_index = 0

        # The following executes the "trickle down" algorithm
        # We run the loop as long as the trickle node has a child
        # that is greater than it.
        while self.has_greater_child(trickle_node_index):
            larger_child_index = self.calculate_larger_child_index(trickle_node_index)
            self.data[trickle_node_index], self.data[larger_child_index] = \
                self.data[larger_child_index], self.data[trickle_node_index]
        return value


    def has_greater_child(self, index):
        # We check whether the node at index has left and right
        # children and if either of those children are greater
        # than the node at index
        return (self.data[self.left_child_index(index)] and self.data[self.left_child_index(index)] > self.data[index]) or \
        (self.data[self.right_child_index(index)] and self.data[self.right_child_index(index)] > self.data[index])


    def calculate_larger_child_index(self, index):
        # If there is no right child
        if not self.data[self.right_child_index(index)]:
            return self.left_child_index(index)

        # If right child value is greater than left child value
        if self.data[self.right_child_index(index)] > self.data[self.left_child_index(index)]:
            # Return right child index
            return self.right_child_index(index)
        # If the left child value is greater than or equal to right child
        else:
            # Return the left child index
            return self.left_child_index(index)

    def get_heap(self):
        return self.data


heap = Heap()
heap_pop_algorithm = []
heap.insert(55)
heap.insert(22)
heap.insert(34)
heap.insert(10)
heap.insert(2)
heap.insert(99)
heap.insert(68)
print(heap.get_heap())
heap_pop_algorithm.append(heap.delete())
heap_pop_algorithm.append(heap.delete())
heap_pop_algorithm.append(heap.delete())
heap_pop_algorithm.append(heap.delete())
heap_pop_algorithm.append(heap.delete())

print(heap_pop_algorithm)
print(heap.get_heap())