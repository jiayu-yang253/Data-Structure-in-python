class Stack:
    def __init__(self):
        self.stack = []
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    def clear(self):
        del self.stack[:]
        
    def dispBottomElement(self):
        print("BottomElement:", self.stack[-1])
        
    def getmax(self):
        max = 0
        for i in range(len(self.stack) - 1, -1, -1):
            if max < self.stack[0]:
                max  = self.stack[i]
        return max
    def getmin(self):
        if self.stack:
            min = self.stack[0]
            for i in range(len(self.stack) - 1, -1, -1):
                if min > self.stack[0]:
                    min  = self.stack[i]
            return min
        else:
            return 0xFFFF
    def getsum(self):
        sum = 0
        for i in range(len(self.stack) - 1, -1, -1):
            sum  += self.stack[i]
        return sum    
    def traverse(self):
        for i in range(len(self.stack) - 1, -1, -1):
            print(self.stack[i])
    
    def search(self,value):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] == value:
                print("Found at index", i, "(0 = bottom)")
                return i
        print("Not found")
    def balancedBrackets(self):
        char = []
        print("Input elements:", end='')
        char = list(map(str, input().split()))
        tempchar = []
        for i in range(len(char) - 1, -1, -1):
            tempchar.append(char[i])
        print("Array:", tempchar)
        tempstack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for i in range(len(tempchar) - 1, -1, -1):
            temp = tempchar[i]
            if not isinstance(temp, str):
                continue
            ch = temp[0]
            if ch in "([{":
                tempstack.append(ch)
                #print("left to bottom:", tempchar[i])
            elif ch in ")]}":
                #print("right to bottom:", tempchar[i])
                if not tempstack or tempstack.pop() != pairs[ch]:
                    return False
        return not tempstack
    def int_to_binary_stack(self,num):
        if num <= 0:
            return "0"
        tempstack = []
        while num > 0:
            remainder = num % 2
            tempstack.append(remainder)
            num = num // 2
        binary_str = ""
        while tempstack:
            binary_str += str(tempstack.pop())
        return binary_str
    def reverseStack(self):
        tempstack = []
        for i in range(len(self.stack) - 1, -1, -1):
            tempstack.append(self.stack[i])
        return tempstack


    
def main_stack_management(stack):
    print("STACK MANAGEMENT SYSTEM")
    print(" 1. Display Stack (top to bottom)")
    print(" 2. Push Element")
    print(" 3. Pop Element")
    print(" 4. Peek Top Element")
    print(" 5. Check Whether Empty")
    print(" 6. Count Elements")
    print(" 7. Search Element")
    print(" 8. Clear Stack")
    print(" 9. Display Bottom Element")
    print(" 10. Find Maximum")
    print(" 11. Find Minimum")
    print(" 12. Calculate Sum")
    print(" 13. Reverse Stack into New Stack")
    print(" 14. Demonstrate Balanced Brackets")
    print(" 15. Decimal to Binary Conversion")
    print(" 16. Exit")
    while True:
        opt = input("\nPlease select task number: ")
        if opt == "1":
            print("Top to bottom:", stack.stack[::-1])
        elif opt == "2":
            val = int(input("Enter element at top: "))
            stack.push(val) 
            print("myStack.pop->", stack.stack)
        elif opt == "3":
            stack.pop() 
        elif opt == "4":
            print("Top peek:", stack.peek())
        elif opt == "5":
            print("Empty:",stack.isEmpty())
        elif opt == "6":
            print("Size:", stack.size())
        elif opt == "7":
            val = int(input("Enter element at start: "))
            stack.search(val) 
        elif opt == "8":
            stack.clear()
        elif opt == "9":
            stack.dispBottomElement()
        elif opt == "10":
            print("Max:", stack.getmax())
        elif opt == "11":
            print("Max:", stack.getmin())
        elif opt == "12":
            print("Sum:", stack.getsum())
        elif opt == "13":
            print("reverse stack:",stack.reverseStack())
        elif opt == '14':
            print(f"Match: {'Balanced' if stack.balancedBrackets() else 'Not balanced'}")
        elif opt == "15":
            val = int(input("Enter element at start: "))
            print("IntDectoBinary:",stack.int_to_binary_stack(val))
        elif opt == "16":
            print("Exit APP") 
            break
        else:
            print("Invalid option, try again.")

def main_menu():
    myStack = Stack()
    myStack.stack.append(10)
    myStack.stack.append(20)
    myStack.stack.append(30)
    print("Stack:", myStack.stack)
    print("Top:", myStack.stack[-1])
    
    myStack.push(40)
    print("myStack.stack", myStack.stack)
    myStack.push(50)
    print("myStack.push(50)->", myStack.stack)
    print("Top:", myStack.stack[-1])
    myStack.pop()
    print("myStack.pop->", myStack.stack)

    while True:
        print("\n===== STACK OPERATIONS =====")
        print("Jiayu Yang,ID:20253801028")
        print("1. Display  2. Push  3. Pop  4. Peek")
        print("5. Is Empty  6. Size 7. STACK MANAGEMENT SYSTEM 8. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            print("Top to bottom:", myStack.stack[::-1])
        elif choice == "2":
            myStack.stack.append(int(input("Value: ")))
            print("Element pushed")
        elif choice == "3":
            print("Popped:", myStack.pop() if myStack.stack else "Underflow")
        elif choice == "4":
            print("Top:", myStack.stack[-1] if myStack.stack else "Stack is empty")
        elif choice == "5":
            print("Empty:", not myStack.stack)
        elif choice == "6":
            print("Size:", len(myStack.stack))
        elif choice == "7":
            main_stack_management(myStack)
        elif choice == "8":
            print("Exit APP") 
            break
        else:
            print("Invalid choice")
        
if __name__ == "__main__":
    main_menu()
