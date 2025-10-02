class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.DELETED = -1

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        initial_index = self.hash_function(key)
        index = initial_index

        while self.table[index] is not None and self.table[index] != self.DELETED:
            if self.table[index] == key:
                print(f"Key {key} already exists in the table.")
                return
            index = (index + 1) % self.size
            if index == initial_index:
                print("Hash table is full. Cannot insert key.")
                return

        self.table[index] = key
        print(f"Key {key} inserted at index {index}.")

    def search(self, key):
        initial_index = self.hash_function(key)
        index = initial_index

        while self.table[index] is not None:
            if self.table[index] == key:
                print(f"Key {key} found at index {index}.")
                return index
            index = (index + 1) % self.size
            if index == initial_index:
                break
        print(f"Key {key} not found in the table.")
        return -1

    def delete(self, key):
        initial_index = self.hash_function(key)
        index = initial_index

        while self.table[index] is not None:
            if self.table[index] == key:
                self.table[index] = self.DELETED
                print(f"Key {key} deleted from index {index}.")
                return
            index = (index + 1) % self.size
            if index == initial_index:
                break
        print(f"Key {key} not found for deletion.")

    def display(self):
        print("\n--- Hash Table ---")
        for i, value in enumerate(self.table):
            if value == self.DELETED:
                print(f"Index {i}: DELETED")
            else:
                print(f"Index {i}: {value}")
        print("--------")

def main():
    size = int(input("Enter the size of the hash table: "))
    ht = HashTable(size)

    while True:
        print("\n----- Hash Table Menu -----")
        print("1. Insert")
        print("2. Search")
        print("3. Delete")
        print("4. Display")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            key = int(input("Enter key (integer): "))
            ht.insert(key)

        elif choice == "2":
            key = int(input("Enter key to search: "))
            ht.search(key)

        elif choice == "3":
            key = int(input("Enter key to delete: "))
            ht.delete(key)

        elif choice == "4":
            ht.display()

        elif choice == "5":
            print("Exiting ")
            break

        else:
            print("Invalid choice ")


if __name__ == "__main__":
    main()
