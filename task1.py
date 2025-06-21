class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        for pair in self.table[key_hash]:
            if pair[0] == key:
                pair[1] = value
                return True
        self.table[key_hash].append(key_value)
        return True

    def get(self, key):
        key_hash = self.hash_function(key)
        for pair in self.table[key_hash]:
            if pair[0] == key:
                return pair[1]
        return None
    
    def delete(self, key):
        key_hash = self.hash_function(key)
        bucket = self.table[key_hash]
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                del bucket[i]
                return True
        return False 

    def __str__(self):
        result = ""
        for i, bucket in enumerate(self.table):
            result += f"{i}: {bucket}\n"
        return result
    


H = HashTable(5)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)
H.delete("banana")


print(H.get("apple"))  
print(H.get("orange")) 
print(H.get("banana")) 

