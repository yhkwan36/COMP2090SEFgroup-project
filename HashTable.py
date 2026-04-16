from typing import Any, List, Optional

class HashTable:
    def __init__(self, initial_size=5):
        self.capacity = initial_size
        self.table = [[] for _ in range(initial_size)]
        self.count = 0

    def _hash(self, key):
        return sum(ord(c) for c in str(key)) % self.capacity

    def _resize(self):
        old_table = self.table
        self.capacity *= 2
        self.table = [[] for _ in range(self.capacity)]
        self.count = 0
        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)

    def insert(self, key, value):
        if self.count / self.capacity > 0.7:
            self._resize()
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])
        self.count += 1

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                self.count -= 1
                return True
        return False

    def contains(self, key):
        return self.get(key) is not None

    def size(self):                  
        return self.count
    