def isEmpty(stk):
    if stk == []:
        return True
    else:
        return False

def Push(stk, item):
    stk.append(item)
    top = len(stk) - 1

def Pop(stk):
    if isEmpty(stk) == True:
        return "UNDERFLOW"
    else:
        item = stk.pop()
        if len(stk) == 0:
            top = None
        else: 
            top = len(stk) - 1
        return item

def Peek(stk):
    if isEmpty(stk) == True:
        return "UNDERFLOW"
    else:
        top = len(stk) - 1
        return stk[top]

def Display(stk):
    if isEmpty(stk):
        print("Stack is Empty")
    else:
        top = len(stk) - 1
        print("Top : ", stk[top])
        for i in range(top-1, -1, -1):
            print(stk[i])


Stack = []
top = None
while True:
    print("STACK OPERATIONS :\n 1. Push\n 2. Pop\n 3. Peek\n 4. Display Stack\n 5. Exit\n")
    choice = int(input("Enter the (No.) Operation you want to do : "))
    if choice == 1:
        element = int(input("Enter element/Item : "))
        Push(Stack, element)
    elif choice == 2:
        element = Pop(Stack)
        if element == "UNDERFLOW":
            print("UNDERFLOW ERROR")
        else:
            print("Removed element : ", element)
    elif choice == 3:
        element = Peek(Stack)
        if element == "UNDERFLOW":
            print("UNDERFLOW ERROR")
        else:
            print("Top element is : ", element)
    elif choice == 4:
        Display(Stack)
    elif choice == 5:
        break
    else:
        print("Please enter a valid operation : ")
