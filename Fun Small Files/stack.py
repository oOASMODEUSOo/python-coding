def ifempty(stk):
    if stk==[]:
        return True
    else:
        return False
#-----------------------------
def Push(stk,item):
    stk.append(item)
    top = len(stk)-1

#-----------------------------------
def Pop(stk):
    if ifempty(stk):
        return("Underflow")
    else:
        item = stk.pop()
        if len(stk) == 0:
            top = None
        else:
            top = len(stk)-1
        return item

#--------------------
def Peek(stk):
    if ifempty(stk):
        return ("Underflow")
    else:
        top = len(stk)-1
        return stk[top]

#---------------------------------
def Display(stk):
    if ifempty(stk):
        print("stack is empty")
    else:
        top = len(stk)-1
        print(stk[top],"<--top")
        for a in range(top-1,-1,-1):
            print(stk[a])

#-----------------------
#__main__
Stack = []
top = None

while True:
    print('stack operation')
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display stack")
    print("5. Exit")
    ch = int(input("enter your choice of operation: "))
    if ch==1:
        item = int(input("Enter Item:"))
        Push(Stack,item)
    elif ch==2:
        item = Pop(Stack)
        if item == "underflow":
            print("Underflow the stack is empty")
        else:
            print("Popped item is",item)
    elif ch == 3:
        item = Peek(Stack)
        if item == "underflow":
            print("underflow stack is empty")
        else:
            print("Topmost item is, ",item)
    elif ch == 4:
        Display(Stack)
    elif ch == 5:
        break
    else:
        print("invalid choice please choose another option")















            
