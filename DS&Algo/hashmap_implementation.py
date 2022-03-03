class MyHashMap(object):

    def __init__(self):
        self.size = 4000
        self.hash = [[]] * self.size

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        hash_value = key % self.size
        if len(self.hash[hash_value]) == 0:
            self.hash[hash_value] = [[key, value]]
        else:
            # Check the hash_value if the key, value exists
            # If it does, then update the value of the key
            for i in range(len(self.hash[hash_value])):
                if self.hash[hash_value][i][0] == key:
                    self.hash[hash_value][i][1] = value
                    return
            self.hash[hash_value].append([key, value])

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        hash_value = key % self.size
        if len(self.hash[hash_value]) == 0:
            return -1
        else:
            for i in range(len(self.hash[hash_value])):
                if self.hash[hash_value][i][0] == key:
                    return self.hash[hash_value][i][1]

        return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash_val = key % self.size

        if len(self.hash[hash_val]) == 0:
            return
        else:
            index = None
            for i in range(len(self.hash[hash_val])):
                if self.hash[hash_val][i][0] == key:
                    index = i
                    break
            if index is not None:
                del self.hash[hash_val][i]

hashmap = MyHashMap()
hashmap.put(1, 1)
hashmap.put(3, 5)
hashmap.put(2, 3)
hashmap.put(9, 2)
hashmap.put(12, 1)
hashmap.put(4, 0)

print(hashmap.get(12))



