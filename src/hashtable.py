class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f'{self.key}: {self.value}'

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.size = 0
        self.old_stor_size = None


    def _hash(self, key):
        return hash(key)

    def _hash_djb2(self, key):                                                                                                                       
        hash = 5381
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF

    def _hash_mod(self, key):
        # checks if the HT has been resized
        if self.old_stor_size is None:
            # if it has not, find modulo of current capacity
            return self._hash(key) % self.capacity
        # else, finds modulo of previous capacity
        return self._hash(key) % self.old_stor_size


    def insert(self, key, value):
        # we hash our key, making out of the key an index
        index = self._hash_mod(key)
        # and we look in our HT at the position the index indicates
        node = self.storage[index]
        # we need to make a while loop to keep checking if the spot in our LL that is on that index is empty
        while node is not None:
            # if it is not, we make a copy of the current node pointer
            temp = node
            # and the current node pointer will point to the current's next node
            node = temp.next
        # when the node is None, it means we have reached the end of the LL, so we create the node..   
        new_node = LinkedPair(key, value)
        # then the new node's next pointer will point to the hashtable's index
        new_node.next = self.storage[index]
        # and the hashtable index will become our new node
        self.storage[index] = new_node
        # we increase the size by 1 since we are just adding one
        self.size += 1
        

    def remove(self, key):
        # we run the hash method to t=determine the index of the node we are trying to remove
        index = self._hash_mod(key)
        # and we reference the hashed key in our HT
        node = self.storage[index]
        # here we check if our spot is not empty, and also if the key doesn't match the key in our node in that spot
        temp = None
        while node.key != key:
            # if it doesn't, means we need to iterate over our LL until we find it, so we assign a temp var copy of our node
            temp = node
            # and we assign the current node to be the next node
            node = temp.next
        # we check if temp is None, meaning the node being deleted is the LL's head..
        if temp is None:
            # we grab the value of the node
            result = node.value
            # we assign the new head to be the next node
            self.storage[index] = node.next
            # and return the deleted node value
            return result
        else:
            self.size -= 1
            # we grab the node's value
            temp.next = node.next
            # return node value
            return node.value


    def retrieve(self, key):
        # we generate the index with our hashed key
        index = self._hash_mod(key)
        # we look in our HT the key we are looking for with our index
        node = self.storage[index]
        # and we check if there is no Node, and if the key
        while node is not None:
            if node.key == key:
                return node.value
            # if it does not match, we iterate
            node = node.next
        # if node ends up being none, there is no node so we return none
        return None

    def resize(self):
        # set's old storage to capacity before increasing it
        self.old_stor_size = self.capacity
        # increase capacity times 2
        self.capacity *= 2
        # we make a new storage with new capacity
        new_storage = [None] * self.capacity
        # we iterate over the old storage
        for i in range(len(self.storage)):
            # we assign each value in current index to the new storage
            new_storage[i] = self.storage[i]
        # we set our new storage to be our storage
        self.storage = new_storage

if __name__ == "__main__":
    ht = HashTable(8)
    ht.insert("key-0", "val-0")
    ht.insert("key-1", "val-1")
    ht.insert("key-2", "val-2")
    ht.insert("key-3", "val-3")
    ht.insert("key-4", "val-4")
    ht.insert("key-5", "val-5")
    ht.insert("key-6", "val-6")
    ht.insert("key-7", "val-7")
    ht.insert("key-8", "val-8")
    ht.insert("key-9", "val-9")
#     ht.resize()
#     # print(ht.retrieve("key-0"))
    print('hastable', ht.storage)