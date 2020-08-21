# Course: CS261 - Data Structures
# Assignment: 5 - Hash Map Implementation
# Student: Rohit Chaudhary
# Description: Hash map implementation using a DynamicArray and LinkedList to handle hash collisions. Methods of put, get, remove, contains_key, clear, empty_buckets, resize_table, table_load, get_keys are implemented.


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with A5 HashMap implementation
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with A5 HashMap implementation
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Init new HashMap based on DA with SLL for collision resolution
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Return content of hash map t in human-readable form
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    def clear(self) -> None:
        """
        function clears all contents of the hash map, current capacity of the hash table is not affected.
        """
        # replace current DynamicArray with a new one of same capacity
        new_table = DynamicArray()
        for i in range(self.capacity):
            new_table.append(LinkedList())
        self.bucket = new_table
        self.size = 0
        return

    def get(self, key: str) -> object:
        """
        function returns the value associated with key. If key is not in the hash map, function returns None.
        """
        hash_index = self.hash_function(key) % self.capacity
        bucket = self.buckets.get_at_index(hash_index)
        # empty bucket
        if bucket.length() == 0:
            return None
        elif bucket.contains(key) != None:  # found key    
            return bucket.contains(key).value
        else:   # key not found in expected chain
            return None

    def put(self, key: str, value: object) -> None:
        """
        function adds the new key:value pair into the hash table. If the key:value pair already exists the hash table, the current value is overwritten with the new value.
        """
        hash_index = self.hash_function(key) % self.capacity
        bucket = self.buckets.get_at_index(hash_index)

        # empty bucket --> add directly
        if bucket.length() == 0:
            bucket.insert(key, value)
            self.size += 1
        # non empty bucket --> check for key
        else:
            if bucket.contains(key): # key present, remove and replace bucket item
                bucket.contains(key).value = value
            else:
                bucket.insert(key, value)
                self.size += 1

        return

    def remove(self, key: str) -> None:
        """
        function removes key and its value from the hash map, otherwise does nothing.
        """
        hash_index = self.hash_function(key) % self.capacity
        bucket = self.buckets.get_at_index(hash_index)
        if bucket.contains(key) != None:  # found key    
            bucket.remove(key)
            self.size -= 1

    def contains_key(self, key: str) -> bool:
        """
        function returns True if key is within the hash map, False otherwise. empty hash table will have no keys, returns False.
        """
        hash_index = self.hash_function(key) % self.capacity
        bucket = self.buckets.get_at_index(hash_index)
        if bucket.length() == 0:
            return False
        elif bucket.contains(key) != None:
            return True
        else:
            return False

    def empty_buckets(self) -> int:
        """
        function returns the number of empty buckets in the table.
        """
        empty = 0
        # if LinkedList chain length is 0, bucket is empty
        for i in range(self.capacity):
            if self.buckets.get_at_index(i).length() == 0:
                empty += 1
        return empty

    def table_load(self) -> float:
        """
        function returns the current load factor of the hash table.
        """
        # lambda = n / m, where n = number of elements and m = number of buckets
        load = self.size / self.capacity
        return load

    def resize_table(self, new_capacity: int) -> None:
        """
        function changes the internal capacity of the hash map to new_capacity. All current key:value pairs remain after function completes. new_capacity less than 1 does nothing.
        """
        if new_capacity < 1:
            return
        else:
            # create a new hashmap that will receive old hash values
            new_map = HashMap(new_capacity, self.hash_function)

            # go through old map and re-hash everything into new map
            for i in range(self.capacity):
                bucket = self.buckets.get_at_index(i)
                # iterate over chains (containing key-value nodes)
                for pair in bucket: 
                    key, value = pair.key, pair.value
                    new_map.put(key, value) # hash into new map
            
            # replace old map with new map
            self.buckets = new_map.buckets
            self.capacity = new_map.capacity
            return
                

    def get_keys(self) -> DynamicArray:
        """
        function returns a DynamicArray instance containing all the keys stored in the current hash map.
        """
        keys = DynamicArray()
        # iterate over the buckets
        for i in range(self.capacity):
            bucket = self.buckets.get_at_index(i)
            # iterate over each chain, getting key
            for item in bucket:
                keys.append(item.key)

        return keys


# BASIC TESTING
# if __name__ == "__main__":

#     print("\nempty_buckets example 1")
#     print("-----------------------------")
#     m = HashMap(100, hash_function_1)
#     print(m.empty_buckets(), m.size, m.capacity)
#     m.put('key1', 10)
#     print(m.empty_buckets(), m.size, m.capacity)
#     m.put('key2', 20)
#     print(m.empty_buckets(), m.size, m.capacity)
#     m.put('key1', 30)
#     print(m.empty_buckets(), m.size, m.capacity)
#     m.put('key4', 40)
#     print(m.empty_buckets(), m.size, m.capacity)


    # print("\nempty_buckets example 2")
    # print("-----------------------------")
    # m = HashMap(50, hash_function_1)
    # for i in range(150):
    #     m.put('key' + str(i), i * 100)
    #     if i % 30 == 0:
    #         print(m.empty_buckets(), m.size, m.capacity)


    # print("\ntable_load example 1")
    # print("--------------------------")
    # m = HashMap(100, hash_function_1)
    # print(m.table_load())
    # m.put('key1', 10)
    # print(m.table_load())
    # m.put('key2', 20)
    # print(m.table_load())
    # m.put('key1', 30)
    # print(m.table_load())


    # print("\ntable_load example 2")
    # print("--------------------------")
    # m = HashMap(50, hash_function_1)
    # for i in range(50):
    #     m.put('key' + str(i), i * 100)
    #     if i % 10 == 0:
    #         print(m.table_load(), m.size, m.capacity)

    # print("\nclear example 1")
    # print("---------------------")
    # m = HashMap(100, hash_function_1)
    # print(m.size, m.capacity)
    # m.put('key1', 10)
    # m.put('key2', 20)
    # m.put('key1', 30)
    # print(m.size, m.capacity)
    # m.clear()
    # print(m.size, m.capacity)


    # print("\nclear example 2")
    # print("---------------------")
    # m = HashMap(50, hash_function_1)
    # print(m.size, m.capacity)
    # m.put('key1', 10)
    # print(m.size, m.capacity)
    # m.put('key2', 20)
    # print(m.size, m.capacity)
    # m.resize_table(100)
    # print(m.size, m.capacity)
    # m.clear()
    # print(m.size, m.capacity)


    # print("\nput example 1")
    # print("-------------------")
    # m = HashMap(50, hash_function_1)
    # for i in range(150):
    #     m.put('str' + str(i), i * 100)
    #     if i % 25 == 24:
    #         print(m.empty_buckets(), m.table_load(), m.size, m.capacity)


    # print("\nput example 2")
    # print("-------------------")
    # m = HashMap(40, hash_function_2)
    # for i in range(50):
    #     m.put('str' + str(i // 3), i * 100)
    #     if i % 10 == 9:
    #         print(m.empty_buckets(), m.table_load(), m.size, m.capacity)


    # print("\ncontains_key example 1")
    # print("----------------------------")
    # m = HashMap(10, hash_function_1)
    # print(m.contains_key('key1'))
    # m.put('key1', 10)
    # m.put('key2', 20)
    # m.put('key3', 30)
    # print(m.contains_key('key1'))
    # print(m.contains_key('key4'))
    # print(m.contains_key('key2'))
    # print(m.contains_key('key3'))
    # m.remove('key3')
    # print(m.contains_key('key3'))


    # print("\ncontains_key example 2")
    # print("----------------------------")
    # m = HashMap(75, hash_function_2)
    # keys = [i for i in range(1, 1000, 20)]
    # for key in keys:
    #     m.put(str(key), key * 42)
    # print(m.size, m.capacity)
    # result = True
    # for key in keys:
    #     # all inserted keys must be present
    #     result &= m.contains_key(str(key))
    #     # NOT inserted keys must be absent
    #     result &= not m.contains_key(str(key + 1))
    # print(result)


    # print("\nget example 1")
    # print("-------------------")
    # m = HashMap(30, hash_function_1)
    # print(m.get('key'))
    # m.put('key1', 10)
    # print(m.get('key1'))


    # print("\nget example 2")
    # print("-------------------")
    # m = HashMap(150, hash_function_2)
    # for i in range(200, 300, 7):
    #     m.put(str(i), i * 10)
    # print(m.size, m.capacity)
    # for i in range(200, 300, 21):
    #     print(i, m.get(str(i)), m.get(str(i)) == i * 10)
    #     print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)


    # print("\nremove example 1")
    # print("----------------------")
    # m = HashMap(50, hash_function_1)
    # print(m.get('key1'))
    # m.put('key1', 10)
    # print(m.get('key1'))
    # m.remove('key1')
    # print(m.get('key1'))
    # m.remove('key4')


    # print("\nresize example 1")
    # print("----------------------")
    # m = HashMap(20, hash_function_1)
    # m.put('key1', 10)
    # print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    # m.resize_table(30)
    # print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))


    # print("\nresize example 2")
    # print("----------------------")
    # m = HashMap(75, hash_function_2)
    # keys = [i for i in range(1, 1000, 13)]
    # for key in keys:
    #     m.put(str(key), key * 42)
    # print(m.size, m.capacity)

    # for capacity in range(111, 1000, 117):
    #     m.resize_table(capacity)

    #     m.put('some key', 'some value')
    #     result = m.contains_key('some key')
    #     m.remove('some key')

    #     for key in keys:
    #         result &= m.contains_key(str(key))
    #         result &= not m.contains_key(str(key + 1))
    #     print(capacity, result, m.size, m.capacity, round(m.table_load(), 2))


    # print("\nget_keys example 1")
    # print("------------------------")
    # m = HashMap(10, hash_function_2)
    # for i in range(100, 200, 10):
    #     m.put(str(i), str(i * 10))
    # print(m.get_keys())

    # m.resize_table(1)
    # print(m.get_keys())

    # m.put('200', '2000')
    # m.remove('100')
    # m.resize_table(2)
    # print(m.get_keys())
