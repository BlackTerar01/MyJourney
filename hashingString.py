"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        self.table[int(self.calculate_hash_value(string))] = self.calculate_hash_value(string)
        """Input a string that's stored in 
        the table."""

    def lookup(self, string):
        if self.calculate_hash_value(string) == self.table[int(self.calculate_hash_value(string))] :
            return self.calculate_hash_value(string)
        # Return the hash value if the
        # string is already in the table.
        # Return -1 otherwise.
        return -1

    def calculate_hash_value(self, string):
        valueList = list(string)
        hashValue = str(ord(valueList[0])) + str(ord(valueList[1]))
        """Helper function to calulate a
        hash value from a string."""
        return hashValue
    
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print (hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print (hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print (hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print (hash_table.lookup('UDACIOUS'))
