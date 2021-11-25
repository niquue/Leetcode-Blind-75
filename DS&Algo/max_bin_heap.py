class MaxBinHeap:

    def __init__(self):
        self.size = 0
        self.array = []
        self.bubble = False
        self.bt = False
        self.parent_found = 0

        self.array[0] = float("NaN")

    def insert(self, element):
        self.array[self.size+1] = element
        new_position = self.size

        while self.array[new_position] > self.array[self.find_parent(new_position)]:
            self.swap(self.find_parent(new_position), new_position)
            new_position = self.find_parent(new_position)

    def get_heap(self):
        return self.array


    def find_parent(self, index):
        return index / 2


    def find_left_child(self, index):
        return index * 2

    def find_right_child(self, index):
        return (2 * index) + 1

    def swap(self, a, b):
        temp = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = temp

    def del_max(self):
        if len(self.array) == 0:
            return

        #double nan as "hole"
        self.array[1] = self.array[self.size]
        self.array[self.size] = 0.0

        i = 1
        self.size -= 1
        while i < self.size:
            left = self.find_left_child(i)
            right = self.find_right_child(i)
            greatest = 0

            if self.array[left] > self.array[right]:
                greatest = left
            else:
                greatest = right

            if self.array[i] < self.array[greatest]:
                self.swap(greatest, i)
            i += 1

    def get_max(self):
        if self.size == 0:
            return float("NaN")
        else:
            return self.array[1]

    def clear(self):
        for i in range(self.size, 1, 1):
            self.array[i] = 0.0
        self.size = 0

    def get_index_array(self, index):
        return self.array[index]

    def size(self):
        return self.size

    def build(self, elements):

        self.clear()

        passed_size = len(elements)
        j = 1
        for i in range(0, len(passed_size), 1):
            self.array[j] = elements[i]
            j += 1
            self.size += 1

        build_node = self.find_parent(passed_size)
        self.parent_found = build_node
        self.build_help(build_node)
        self.bubble = False
        self.bt = False

    def build_help(self, index):
        if index == 0 and not self.bubble:
            self.bubble = True
            self.build_help(self.parent_found)

        if index == 0 and self.bubble and not self.bt:
            self.bt = True
            self.build_help(self.parent_found)

        get_left = self.find_left_child(index)
        get_right = self.find_right_child(index)
        greater = 0

        if index > 0 and self.array[get_left] > self.array[get_right]:
            greater = get_left
        elif index > 0 and self.array[get_right] > self.array[get_left]:
            greater = get_right

        if index != greater:
            if self.array[greater] > self.array[index]:
                self.swap(greater, index)
            self.build_help(index - 1)
        else:
            pass

    def sort(self, elements):

        self.clear()
        temp_array = []
        return_array = []

        self.build(elements)
        for i in range(len(elements), -1, -1):
            return_array[i] = self.get_max()
            self.del_max()

        self.build(elements)
        self.clear()
        return return_array


def test_sort():
    mbh = MaxBinHeap()
    collection = [3, 8, 2, 1, 7, 4, 5, 6]
    sorted = mbh.sort()
    print_sort_collection(collection)
    print_heap(mbh.get_heap(), mbh.size())


def print_sort_collection(e):
    print("Printing Collection to pass in to heap sort function:")
    for i in range(0, len(e), 1):
        print(e[i] + '\t')
    print('\n')

def print_heap(e, length):
    print("Printing Heap")
    for i in range(1, len(length), 1):
        print(e[i] + '\t')
    print('\n')

test_sort()