class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return key % self.size
        
    def insert(self, key, value):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                print(f"Updated key {key} with value {value}")
                return
                
        self.table[index].append([key, value])
        print(f"Inserted key {key} with value {value}")


    def search(self, key):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None 
    
    def delete(self, key):
        index = self._hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                print(f"Deleted key {key}")
                return
        print(f"key {key} not found for deletion.")

    def display(self):
        print("Hash Table: ")
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")


def main():
    ht = HashTable(10)  

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
            value = input("Enter value: ")
            ht.insert(key, value)

        elif choice == "2":
            key = int(input("Enter key to search: "))
            result = ht.search(key)
            if result is not None:
                print(f"Found: Key {key} -> Value {result}")
            else:
                print(f"Key {key} not found.")

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
