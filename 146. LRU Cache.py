class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.keys = []



        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache[key]
        else:
            return -1
        
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.keys.remove(key)
            self.keys.append(key)
            self.cache[key] = value
        else:
            if len(self.keys) == self.capacity:
                del self.cache[self.keys[0]]
                self.keys.pop(0)
            self.keys.append(key)
            self.cache[key] = value

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)