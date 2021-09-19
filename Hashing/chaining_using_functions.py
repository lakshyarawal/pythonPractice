
""" Collision handling using Chaining: Implementation of chaining using Linked List and chain creation"""


def display_hash(hash_table):  # Function to display hashtable
    for i in range(len(hash_table)):
        print(i, end=" ")

        for j in hash_table[i]:
            print("-->", end=" ")
            print(j, end=" ")
        print()


# Hashing Function to return
# key for every value.
def hashing(key_value, hash_table):
    return key_value % len(hash_table)


# Insert Function to add
# values to the hash table
def insert(hash_table, key_value, value):
    hash_key = hashing(key_value, hash_table)
    hash_table[hash_key].append(value)


# Delete Function to remove
# values to the hash table
def delete(hash_table, key_value, value):
    hash_key = hashing(key_value, hash_table)
    hash_table[hash_key].remove(value)


def main():
    # Driver Code
    # Creating Hashtable as
    # a nested list.
    hash_table = [[] for _ in range(10)]
    insert(hash_table, 10, 'Allahabad')
    insert(hash_table, 25, 'Mumbai')
    insert(hash_table, 20, 'Lucknow')
    insert(hash_table, 9, 'Delhi')
    insert(hash_table, 21, 'Punjab')
    insert(hash_table, 21, 'Noida')
    display_hash(hash_table)
    delete(hash_table, 21, 'Punjab')
    display_hash(hash_table)


if __name__ == "__main__":
    main()
