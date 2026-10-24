class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new = Node(value)
        if self.head is None:
            self.head = self.tail = new
        else:
            new.prev = self.tail
            self.tail.next = new
            self.tail = new
    
    def display_forward(self):
        current = self.head
        while current is not None:
            print(current.data, end=" <-> " if current.next else "")
            current = current.next
        print()

    def display_backward(self):
        current = self.tail
        while current is not None:
            print(current.data, end=" <-> " if current.prev else "")
            current = current.prev
        print()

    def prepend(self, value):
        new = Node(value)
        if self.head is None:
            self.head = self.tail = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new
            
    def insert_at(self, index, value):
        if index < 0:
            return False
        if index == 0:
            self.prepend(value)
            return True
        current = self.head
        position = 0
        while current is not None and position < index:
            current = current.next
            position += 1
        if position != index:
            return False
        if current is None:
            self.append(value)
            return True
        new = Node(value)  
        before = current.prev  # 
        new.prev = before
        new.next = current
        before.next = new
        current.prev = new
        return True
    
    def insert_at_position(self, index, value):
        new = Node(value)
        if index == 1:
            new.next = self.head
            if self.head:
                self.head.prev = new
            return new
        
        temp = self.head
        for _ in range(index-1):
            temp = temp.next
        
        next_node = temp.next
        new.next = next_node
        new.prev = temp
        temp.next = new
        next_node.prev = new
        return self
        
    def delete_first(self):
        if self.head is None:
            return None
        value = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        return value

    def delete_last(self):
        if self.tail is None:
            return None
        value = self.tail.data
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        return value
    
    def search(self, value):
        current = self.head
        index = 0
        while current is not None:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1

    def update_at(self, index, new_value):
        if index < 0:
            return False
        current = self.head
        for _ in range(index):
            if current is None:
                return False
            current = current.next
        if current is None:
            return False
        current.data = new_value
        return True
    
    def delete_value(self, value):
        current = self.head
        while current is not None and current.data != value:
            current = current.next
        if current is None:
            return False
        if current.prev is None:
            self.head = current.next
        else:
            current.prev.next = current.next
        if current.next is None:
            self.tail = current.prev
        else:
            current.next.prev = current.prev
        return True
    def delete_at(self, position):
        if position < 0 or self.head is None:
            return False
        if position == 0:
            self.head.next.prev = None
            self.head = self.head.next
            return True
        previous = self.head
        for _ in range(position - 1):
            if previous.next is None:
                return False
            previous = previous.next
        if previous.next is None:
            self.tail = previous.prev
            return False
        if previous.next.next is None:
            self.tail = self.tail.prev
            if self.tail is None:
                self.head = None
            else:
                self.tail.next = None
            return True
        previous.next.next.prev = previous.next.prev
        previous.next = previous.next.next
        return True
    def count(self):
        total = 0
        odd  = 0
        even = 0
        current = self.head
        while current is not None:
            total += 1
            if current.data % 2 == 1:
                odd += 1
            else:
                even += 1
            current = current.next
        return total,odd,even

    def reverse(self):
        current = self.head
        while current is not None:
            current.prev, current.next = current.next, current.prev
            current = current.prev
        self.head, self.tail = self.tail, self.head
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
        n,odd,even = self.count()
        if n == 0:
            return None
        return self.get_sum() / n
    def insert_after(self, value, newValue):
        current = self.head
        position = 0
        while current is not None:
            current = current.next
            position += 1
            if current.data == value:
                break
        if current is None:
            self.append(newValue)
            return True
        new = Node(newValue)  
        new.next = current
            
        new = Node(newValue)  
        after = current.prev  # 
        new.prev = after
        new.next = current
        after.next = new
        current.prev = new
        return True
    def find_middleNode(self):
        if self.head is None:
            return None
        slow = self.head
        fast = self.head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.data  # for even length this returns the first of the two middles
    def remove_duplicate(self):
        seen = set()
        current = self.head
        while current is not None:
            nxt = current.next
            if current.data in seen:
                if current.prev is None:
                    self.head = current.next
                else:
                    current.prev.next = current.next
                if current.next is None:
                    self.tail = current.prev
                else:
                    current.next.prev = current.prev
            else:
                seen.add(current.data)
            current = nxt
    
def main_list_management(dLinedList):
    
    print("DOUBLY LINKED LIST MANAGEMENT")
    print(" 1. Display Forward")
    print(" 2. Display Backward")
    print(" 3. Insert at Beginning")
    print(" 4. Insert at End")
    print(" 5. Insert at Index")
    print(" 6. Delete First")
    print(" 7. Delete Last")
    print(" 8. Delete by Value")
    print(" 9. Delete by Index")
    print("10. Search Value")
    print("11. Update by Index")
    print("12. Count Nodes")
    print("13. Sum / Min / Max / Average")
    print("14. Reverse List")
    print("15. Exit")
    while True:
        opt = input("\nPlease select task number: ")
        if opt == "1":
            dLinedList.display_forward()
        elif opt == "2":
            dLinedList.display_backward() 
        elif opt == "3":
            val = int(input("Enter element at start: "))
            dLinedList.prepend(val)
            dLinedList.display_forward()
        elif opt == "4":
            val = int(input("Enter element at end: "))
            dLinedList.append(val)
            dLinedList.display_forward()
        elif opt == "5":
            index = int(input("Enter index: "))
            val = int(input("Enter element: "))
            if dLinedList.insert_at(index,val):
                dLinedList.display_forward()
            else:
                print("insert failed,index error")
        elif opt == "6":
            dLinedList.delete_first()
            dLinedList.display_forward()
        elif opt == "7":
            dLinedList.delete_last()
            dLinedList.display_forward()
        elif opt == "8":
            value = int(input("Enter value to delete: "))
            if dLinedList.delete_value(value):
                dLinedList.display_forward()
            else:
                print("delete at failed")
        elif opt == "9":
            index = int(input("Enter index to delete: "))
            if dLinedList.delete_at(index):
                dLinedList.display_forward()
            else:
                print("delete at failed")
        elif opt == "10":
            val = int(input("Enter element to search: "))
            if dLinedList.search(val) != -1:
               print("search value success") 
            else:
               print("search value failed") 
        elif opt == "11":
            index = int(input("Enter data to index: "))
            val = int(input("Enter element to add: "))
            if dLinedList.update_at(index,val):
                print("update value success")
            else:
                print("update value failed") 
        elif opt == "12":
            dLinedList.display_forward()
            print("count_nodes:", dLinedList.count())
        elif opt == "13":
            dLinedList.display_forward()
            print("get_max value:", dLinedList.get_max())
            print("get_min value:", dLinedList.get_min())
            print("total_value:", dLinedList.get_sum())
            print("average_value:", dLinedList.get_average())
        elif opt == '14':
            dLinedList.display_forward()
            dLinedList.reverse()
            dLinedList.display_forward()
        elif opt == "15":
            print("Exit APP") 
            break
        else:
            print("Invalid option, try again.")

def main_menu():
    first = Node(10)
    second = Node(20)
    first.next = second
    second.prev = first
    print(first.next.data)   # 20
    print(second.prev.data)  # 10  
    
    dll = DoublyLinkedList()   
    for number in [10, 20, 30]:
        dll.append(number)
    dll.display_forward()   # 10 <-> 20 <-> 30
    dll.display_backward()  # 30 <-> 20 <-> 10
    
    dll.prepend(5)         
    dll.display_forward()   #5 <-> 10 <-> 20 <-> 30
    dll.insert_at(2, 15)    
    dll.display_forward()   #5 <-> 10 <-> 15 <-> 20 <-> 30
    
    dll.delete_first()      
    dll.display_forward()   # 10 <-> 15 <-> 20 <-> 30
    dll.delete_last() 
    dll.display_forward()   # 10 <-> 15 <-> 20 
    print("searched index: ",dll.search(20))  #searched index: 2
    dll.update_at(2, 25)
    dll.display_forward()
    dll.delete_value(25)
    dll.display_forward()
    print("count: ",dll.count()) #count: 2
    dll.reverse()
    dll.display_forward()   # 30 <-> 25 <-> 10 <-> 5

    print(" 1. Entry Main Doubly Linked List_management")
    print(" 2. Remove precisely the selected node")
    print(" 3. Insert after the first matching node")
    print(" 4. Find the middle node")
    print(" 5. Remove duplicate values")
    while True:
        opt = input("\nPlease select task number: ")
        if opt == "1":
            main_list_management(dll)
        elif opt == "2":#challenge delete_at
            index = int(input("Enter index to delete: "))
            if dll.delete_at(index):
                dll.display_forward()
            else:
                print("delete at failed")
        elif opt == "3":   #challenge delete_at
            value = int(input("Enter find value: "))
            newValue = int(input("insert newValue: "))
            dll.insert_after(value,newValue)
            dll.display_forward()
        elif opt == "4":   #challenge find_middleNode
            dll.find_middleNode()
            dll.display_forward()
        elif opt == "5":   #challenge remove_duplicate
            dll.remove_duplicate()
            dll.display_forward()
        
        
if __name__ == "__main__":
    main_menu()
