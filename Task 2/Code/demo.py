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
    
def partition(arr: List[Any], low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quicksort(arr: List[Any], low: int = 0, high: Optional[int] = None) -> List[Any]:
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)
    return arr

if __name__ == "__main__":
    print("=== HASH TABLE DEMO ===")
    ht = HashTable()
    ht.insert("apple", 1)
    ht.insert("banana", 2)
    ht.insert("cherry", 3)
    ht.insert("date", 4)
    ht.insert("elderberry", 5)
    ht.insert("fig", 6)          
    print("HashTable contents:", ht)
    print("get('banana') =", ht.get("banana"))
    print("contains('fig') =", ht.contains("fig"))
    print("size() =", ht.size())           
    ht.delete("cherry")
    print("After deleting cherry, size =", ht.size())

    print("\n=== QUICKSORT DEMO ===")
    data = [10, 7, 8, 9, 1, 5]
    print("Original:", data)
    sorted_data = quicksort(data)
    print("Sorted:", sorted_data)