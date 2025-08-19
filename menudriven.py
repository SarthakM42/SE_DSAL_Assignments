def fetch_id():
    list1 = []
    num_of_ID = int(input("Enter number of IDs you want to fetch: "))
    for i in range(num_of_ID):
        id_num = int(input("Enter Account ID: "))
        list1.append(id_num)
    return list1

def linear_search(list_, n1):
    for i in range(len(list_)):
        if list_[i] == n1:
            return i 
    return -1  

def binary_search(list_, AC_ID):
    list_.sort()
    print("Sorted list:", list_)
    
    left = 0
    right = len(list_) - 1
    while left <= right:
        mid = (left + right) // 2
        if list_[mid] == AC_ID:
            print(f"{AC_ID} found at index {mid}")
            return mid
        elif list_[mid] < AC_ID:
            left = mid + 1
        else:
            right = mid - 1
    print("Element not found")
    return -1

def main():
    while True:
        print("\nFetch Account IDs")
        list1 = fetch_id()
        
        print("\nSearch Account ID using: ")
        print("1. Linear search")
        print("2. Binary search")
        print("3. Exit")
        
        choice = int(input("Enter your choice (1/2/3): "))
        
        if choice==1:
            n1=int(input("Enter AC.ID to be searched: "))
            index=linear_search(list1, n1)
            if index !=-1:
                print(f"Element found at index {index}")
            else:
                print("Element not found")
        elif choice==2:
            AC_ID=int(input("Enter AC.ID to be searched: "))
            binary_search(list1, AC_ID)
        elif choice==3:
            print("Program terminated")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
