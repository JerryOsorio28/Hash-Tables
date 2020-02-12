class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.size = 0
        self.old_stor_size = None


    def _hash(self, key):
        return hash(key)

    def _hash_mod(self, key):
        # checks if the HT has been resized
        if self.old_stor_size is None:
            # if it has not, find modulo of current capacity
            return self._hash(key) % self.capacity
        # else, finds modulo of previous capacity
        return self._hash(key) % self.old_stor_size


    def insert(self, key, value):
        index = self._hash_mod(key)
        # and we look in our HT at the position the index indicates
        node = self.storage[index]
        # if it is, we need to make a while loop to keep checking if the spot in our LL that is on that index is empty
        while node is not None and node.key != key:
            # if it is not, we make a copy of the current node pointer
            temp = node
            # and the current node pointer will point to the current's next node
            node = node.next
        # we check if it is empty..
        if node is not None:
            node.value = value
        else:
            new_node = LinkedPair(key, value)
            # if it is, we create the node on that index and return
            new_node.next = self.storage[index]
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
        # if node is not, it means we did not found the node we want to delete, and we return None
        if node is None:
            return None
        # if we find our node...
        else:
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
    ht.resize()
    print(ht.retrieve("key-0"))