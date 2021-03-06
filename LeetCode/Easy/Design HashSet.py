class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashSet=set()

    def add(self, key: int) -> None:
        self.hashSet.add(key)

    def remove(self, key: int) -> None:
        self.hashSet.discard(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.hashSet:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashMap=[-1]*1000000
        
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.hashMap[key]=value

        #self.hashMap[key]=value
        
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if self.hashMap[key]!=-1:
            return self.hashMap[key]
        else:
            return -1
        
        #if key in self.hashMap:
        #    return self.hashMap[key]
        #else:
        #    return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.hashMap[key]=-1

        #if key in self.hashMap:
        #    del self.hashMap[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
