class ChainingHashTable:
    def __init__(self):
        self.size = 10
        self.table = []
        for i in range(self.size):
            self.table.append([])

    def insert(self, key, val):
        key_hash = hash(key) % len(self.table)
        key_value = (key, val)

        if not self.table[key_hash]:
            self.table[key_hash].append(key_value)
        else:
            for key_value_pair in self.table[key_hash]:
                if key_value_pair[0] == key:
                    key_value_pair[1] = val
                    return
            self.table[key_hash].append(key_value)

    def lookup(self, key):
        key_hash = hash(key) % len(self.table)
        
        if self.table[key_hash]:
            for key_value_pair in self.table[key_hash]:
                if key_value_pair[0] == key:
                    return key_value_pair[1]
            return None
        else:
            return None

