"""
Lab: singly_linked_list
All Tasks in one project
"""

#A Lisked List node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        print("List: ", end="")
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        return True
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        return True
    def insert_at(self, position, value):
        if position < 0:
            return False
        if position == 0:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            return True
        previous = self.head
        for _ in range(position - 1):
            if previous is None:
                return False
            previous = previous.next
        if previous is None:
            return False
        new_node = Node(value)
        new_node.next = previous.next
        previous.next = new_node
        return  True
    def delete_value(self, value):
        if self.head is None:
            return False
        if self.head.data == value:
            self.head = self.head.next
            return True
        previous = self.head
        while previous.next:
            if previous.next.data == value:
                previous.next = previous.next.next
                return True
            previous = previous.next
        return False
    def delete_at(self, position):
        if position < 0 or self.head is None:
            return False
        if position == 0:
            self.head = self.head.next
            return True
        previous = self.head
        for _ in range(position - 1):
            if previous.next is None:
                return False
            previous = previous.next
        if previous.next is None:
            return False
        previous.next = previous.next.next
        return True
    def search(self, value):
        position = 0
        current = self.head
        while current is not None:
            if current.data == value:
                return position
            current = current.next
            position += 1
        return -1
    def update_at(self, position, new_value):
        if position < 0:
            return False
        current = self.head
        for _ in range(position):
            if current is None:
                return False
            current = current.next
        if current is None:
            return False
        current.data = new_value
        return True
    def count_nodes(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    def count_even_nodes(self):
        count = 0
        current = self.head
        while current:
            if current.data%2 == 0:
                count += 1
            current = current.next
        return count       
    def count_odd_nodes(self):
        count = 0
        current = self.head
        while current:
            if current.data%2:
                count += 1
            current = current.next
        return count
    def get_sum(self):
        total = 0
        current = self.head
        while current:
            total += current.data
            current = current.next
        return total
    def get_max(self):
        if self.head is None:
            return None
        max_val = self.head.data
        current = self.head.next
        while current:
            if current.data > max_val:
                max_val = current.data
            current = current.next
        return max_val
    def get_min(self):
        if self.head is None:
            return None
        min_val = self.head.data
        current = self.head.next
        while current:
            if current.data < min_val:
                min_val = current.data
            current = current.next
        return min_val
    def get_average(self):
        n = self.count_nodes()
        if n == 0:
            return None
        return self.get_sum() / n
    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous
    def get_first(self):
        return self.head.data if self.head else None
    def get_last(self):
        if self.head is None:
            return None
        current = self.head
        while current.next:
            current = current.next
        return current.data

def userInput_DispListedList():  
    listedList = LinkedList()
    print("Jiayu Yang,ID:20253801028")
    print("\n===== createLinkedList: Create and Display an ListedList =====")
    print("Input 10 elements:")
    numbers = list(map(int, input().split()))
    for n in numbers:
        listedList.append(n)
    print("List: ", end="")
    listedList.display()
    print(f"First: {listedList.get_first()}  Last: {listedList.get_last()}")
    return listedList
    
def main_list_management(listedlist):
    listedlist.display()
    print("singly linked list management system")
    while True:
        print(" 1: Display linked list")
        print(" 2: Add Node at End")
        print(" 3: Add Node at Beginning")
        print(" 4: Insert Node at Position")
        print(" 5: Delete Node by Position")
        print(" 6: Delete Node by Value")
        print(" 7: Search Node")
        print(" 8: Update Node")
        print(" 9: Count Nodes")
        print("10: Find Maximum")
        print("11: Find Minimum")
        print("12: Calculate Sum")
        print("13: Calculate Average")
        print("14: Reverse List")
        print("15: Exit")
        opt = input("\nPlease select task number: ")
  
        if opt == "1":
            listedlist.display()
        elif opt == "2":
            val = int(input("Enter element to add: "))
            if listedlist.append(val):
                listedlist.display()
            else:
                print("append failed")
        elif opt == "3":
            val = int(input("Enter element to add: "))
            if listedlist.prepend(val):
                listedlist.display()
            else:
                print("preappend failed")
        elif opt == "4":
            index = int(input("Enter data to index: "))
            val = int(input("Enter element to add: "))
            if listedlist.insert_at(index,val):
                listedlist.display()
            else:
                print("insert failed")
        elif opt == "5":
            index = int(input("Enter index to delete: "))
            if listedlist.delete_at(index):
                listedlist.display()
            else:
                print("delete at failed")
        elif opt == "6":
            val = int(input("Enter element to delete: "))
            if listedlist.delete_value(val):
                listedlist.display()
            else:
                print("delete value failed")
        elif opt == "7":
            listedlist.display()
            val = int(input("Enter element to search: "))
            if listedlist.search(val) != -1:
               print("search value success") 
            else:
               print("search value failed") 
        elif opt == "8":
            listedlist.display()
            index = int(input("Enter data to index: "))
            val = int(input("Enter element to add: "))
            if listedlist.update_at(index,val):
                print("update value success")
            else:
                print("update value failed") 
        elif opt == "9":
            print("count_nodes:", listedlist.count_nodes())
            print("count_odd_nodes:", listedlist.count_odd_nodes())
            print("count_even_nodes:", listedlist.count_even_nodes())
        elif opt == "10":
            print("get_max value:", listedlist.get_max())
        elif opt == "11":
            print("get_min value:", listedlist.get_min())
        elif opt == "12":
            print("total_value:", listedlist.get_sum())
        elif opt == "13":
            print("average_value:", listedlist.get_average())
        elif opt == "14":
            listedlist.display()
            listedlist.reverse()
            listedlist.display()
        elif opt == "15":
            print("linked list management system")
            break
        else:
            print("Invalid option, try again.")
            
def main_menu():
    
    #default singly linked list
    myListedList = LinkedList()
    myListedList.append(10)
    myListedList.append(20)
    myListedList.append(30)
    myListedList.append(40)
    myListedList.append(60)
    myListedList.display()
    print("\n======== LAB MAIN MENU ========")
    print(" 1: Create & Display linked list")
    print(" 2: Add Node at End")
    print(" 3: Add Node at Beginning")
    print(" 4: Insert Node at Position")
    print(" 5: Delete Node by Position")
    print(" 6: Delete Node by Value")
    print(" 7: Search Node")
    print(" 8: Update Node")
    print(" 9: Count Nodes")
    print("10: Maximum,Minimum,Sum,Average")
    print("11: Reverse List")
    print("12: linked list management system")
    print("13: Exit")
    
    while True:
        opt = input("\nPlease select task number: ")
  
        if opt == "1":
            myListedList = userInput_DispListedList()
        elif opt == "2":
            val = int(input("Enter element to add: "))
            if myListedList.append(val):
                myListedList.display()
            else:
                print("append failed")
        elif opt == "3":
            val = int(input("Enter element to add: "))
            if myListedList.prepend(val):
                myListedList.display()
            else:
                print("preappend failed")
        elif opt == "4":
            index = int(input("Enter data to index: "))
            val = int(input("Enter element to add: "))
            if myListedList.insert_at(index,val):
                myListedList.display()
            else:
                print("insert failed")
        elif opt == "5":
            index = int(input("Enter index to delete: "))
            if myListedList.delete_at(index):
                myListedList.display()
            else:
                print("delete at failed")
        elif opt == "6":
            val = int(input("Enter element to delete: "))
            if myListedList.delete_value(val):
                myListedList.display()
            else:
                print("delete value failed")
        elif opt == "7":
            myListedList.display()
            val = int(input("Enter element to search: "))
            if myListedList.search(val) != -1:
               print("search value success") 
            else:
               print("search value failed") 
        elif opt == "8":
            myListedList.display()
            index = int(input("Enter data to index: "))
            val = int(input("Enter element to add: "))
            if myListedList.update_at(index,val):
                print("update value success")
            else:
                print("update value failed") 
        elif opt == "9":
            print("count_nodes:", myListedList.count_nodes())
            print("count_odd_nodes:", myListedList.count_odd_nodes())
            print("count_even_nodes:", myListedList.count_even_nodes())
        elif opt == "10":
            print("get_max value:", myListedList.get_max())
            print("get_min value:", myListedList.get_min())
            print("total_value:", myListedList.get_sum())
            print("average_value:", myListedList.get_average())
        elif opt == "11":
            myListedList.display()
            myListedList.reverse()
            myListedList.display()
        elif opt == "12":
            main_list_management(myListedList)
        elif opt == "13":
            print("Exit APP") 
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main_menu()
