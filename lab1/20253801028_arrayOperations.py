"""
Lab: Array Operations
All Tasks in one project
Task1‑Task9, Main Assignment, Challenge Task, Advanced Tasks
Discussion Questions answers are in comments at bottom of file
"""
def task1():
    print("Jiayu Yang,ID:20253801028")
    print("\n===== Task1: Create and Display an Array =====")
    numbers = []
    print("Input 10 elements:")
    numbers = list(map(int, input().split()))
    print("Array:", numbers)
    print("First element:", numbers[0])
    print("Last element:", numbers[9])
    return numbers

def task2(array):
    print("\n===== Task2: Addition =====") 
    print("Before:", array)
    new_val = int(input("Enter value: "))
    array.append(new_val)
    print("After:", array)

def task3(array):
    print("\n===== Task3: Insertion =====")
    length = len(array)
    val = int(input("Value: "))
    idx = int(input("Index: "))
    if idx>length:
       print("Invalid index") 
    else:
       array.insert(idx, val)
    print(array)

def task4(array):
    print("\n===== Task4: Deletion =====")
    del_idx = int(input("Enter index to delete: "))
    array.pop(del_idx)
    print(array)

def task5(array):
    print("\n===== Task5: Searching =====")
    search_val = int(input("Enter value: "))
    if search_val in array:
        pos = array.index(search_val)
        print(f"Element found at index {pos}")
    else:
        print("Element not found")

def task6(array):
    print("\n===== Task6: Update an Element =====")
    idx = int(input("Index: "))
    new_val = int(input("New value: "))
    array[idx] = new_val
    print(array)

def task7(array):
    print("\n===== Task7: Sum and Average =====")
    total = sum(array)
    average = total / len(array)
    maximum = max(array)
    minimum = min(array)
    print("Sum:", total)
    print("Average:", average)
    print("Maximum:", maximum)
    print("Minimum:", minimum)

def task8(array):
    print("\n===== Task8: Count Even and Odd Numbers =====")
    even_count = 0
    odd_count = 0
    for i in range(10):
        v = array[i]
        if v % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print("Array:", array)
    print("Even numbers:", even_count)
    print("Odd numbers:", odd_count)

def task9(array):
    print("\n===== Task9: Sort and Reverse an Array =====")
    print("Original:")
    print(array)
    array.sort()
    print("Sort:")
    print(array)
    array.reverse()
    print("Reverse:")
    print(array)

def main_array_management(array):
    print("\n===== Main Lab Assignment: Array Management System =====")
    arr = array
    while True:
        print("====================================")
        print("      ARRAY MANAGEMENT SYSTEM")
        print("====================================")
        print("1. Display Array")
        print("2. Add Element")
        print("3. Insert Element")
        print("4. Delete by Index")
        print("5. Delete by Value")
        print("6. Search Element")
        print("7. Update Element")
        print("8. Find Maximum")
        print("9. Find Minimum")
        print("10. Calculate Sum")
        print("11. Calculate Average")
        print("12. Sort and Reverse Array")
        print("13. Exit this subsystem")

        choice = input("Enter your choice: ")
        print("Array:", arr)
        if choice == "1":
            print("Array:", arr)
        elif choice == "2":
            val = int(input("Enter element to add: "))
            arr.append(val)
            print("Element added.")
        elif choice == "3":
            idx = int(input("Enter index: "))
            val = int(input("Enter value: "))
            if 0 <= idx <= len(arr):
                arr.insert(idx, val)
                print("Element inserted.")
            else:
                print("Invalid index")
        elif choice == "4":
            idx = int(input("Enter index to delete: "))
            if 0 <= idx < len(arr):
                removed = arr.pop(idx)
                print(f"Deleted value: {removed}")
            else:
                print("Invalid index")
        elif choice == "5":
            val = int(input("Enter value to delete: "))
            if val in arr:
                arr.remove(val)
                print(f"Value {val} removed")
            else:
                print("Value not found")
        elif choice == "6":
            val = int(input("Enter value to search: "))
            if val in arr:
                pos = arr.index(val)
                print(f"Found at index {pos}")
            else:
                print("Element not found")
        elif choice == "7":
            idx = int(input("Enter index to update: "))
            if 0 <= idx < len(arr):
                new_val = int(input("Enter new value: "))
                arr[idx] = new_val
                print("Updated successfully")
            else:
                print("Invalid index")
        elif choice == "8":
            if len(arr) == 0:
                print("Array is empty")
            else:
                print("Maximum:", max(arr))
        elif choice == "9":
            if len(arr) == 0:
                print("Array is empty")
            else:
                print("Minimum:", min(arr))
        elif choice == "10":
            print("Sum:", sum(arr))
        elif choice == "11":
            if len(arr) == 0:
                print("Array is empty")
            else:
                avg = sum(arr)/len(arr)
                print("Average:", avg)
        elif choice == "12":
            arr.sort()
            print("Array sorted:", arr)
            arr.reverse()
            print("Array reversed:", arr)
        elif choice == "13":
            print("Exit Array Management System")
            break
        else:
            print("Invalid choice, try again.")

def challenge_task(array):
    print("\n===== Challenge Task: Manual sum/max/min (no built‑in functions) =====")
    print("Test array:", array)
    total = 0
    for num in array:
        total = total + num
    max_val = array[0]
    min_val = array[0]
    for n in array:
        if n > max_val:
            max_val = n
        if n < min_val:
            min_val = n
    average = total / len(array)
    print("Manual Sum:", total)
    print("Manual Max:", max_val)
    print("Manual Min:", min_val)
    print("Manual Average:", average)

def advanced_manual_insert(array):
    print("\n===== Advanced Task: Manual Insertion (no insert()) =====")
    insert_index = int(input("Index: "))
    insert_value = int(input("Value: "))
    new_arr = []
    for i in range(len(array)):
        if i == insert_index:
            new_arr.append(insert_value)
        new_arr.append(array[i])
    print("Original:", array)
    print("After manual insert:", new_arr)


def advanced_manual_delete(array):
    print("\n===== Advanced Task: Manual Deletion (no pop/remove/del) =====")
    delete_index = int(input("Index: "))
    new_arr = []
    for i in range(len(array)):
        if i != delete_index:
            new_arr.append(array[i])
    print("Original:", array)
    print("After manual delete:", new_arr)

def main_menu():
    numbers_array = [10, 20, 30, 40, 60]
    print("\n======== LAB MAIN MENU ========")
    print(" 1: Task1  Create & Display Array")
    print(" 2: Task2  Addition")
    print(" 3: Task3  Insertion")
    print(" 4: Task4  Deletion")
    print(" 5: Task5  Searching")
    print(" 6: Task6  Update Element")
    print(" 7: Task7  Sum / Avg / Max / Min")
    print(" 8: Task8  Count Even Odd")
    print(" 9: Task9  Sort and Reverse Array")
    print("10: Main Assignment - Array Management System")
    print("11: Challenge Task Manual Sum Max Min")
    print("12: Advanced Task Manual Insert")
    print("13: Advanced Task Manual Delete")
    print(" 0: Exit entire program")
    while True:
        opt = input("\nPlease select task number: ")
        if opt == "1":
            numbers_array = task1()
        elif opt == "2":
            task2(numbers_array)
        elif opt == "3":
            task3(numbers_array)
        elif opt == "4":
            task4(numbers_array)
        elif opt == "5":
            task5(numbers_array)
        elif opt == "6":
            task6(numbers_array)
        elif opt == "7":
            task7(numbers_array)
        elif opt == "8":
            task8(numbers_array)
        elif opt == "9":
            task9(numbers_array)
        elif opt == "10":
            main_array_management(numbers_array)
        elif opt == "11":
            challenge_task(numbers_array)
        elif opt == "12":
            advanced_manual_insert(numbers_array)
        elif opt == "13":
            advanced_manual_delete(numbers_array)
        elif opt == "0":
            print("Program finished.")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main_menu()


