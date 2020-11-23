
#---------------------------
def Push(stk,item):
    stk.append(item)
    return stk

def Pop(stk):
    item = stk.pop()
    if len(stk) == 0:
        top = None
    else:
        top = len(stk)-1
    return item  
#----------------------------------  

Stack=[]
while True:
    print("action on stacks")
    print("1. Push")
    print("2. Pop")
    print("3. display")
    ch=int(input("enter the operation"))
    if ch==1:
        item = int(input("Enter Item:"))
        Push(Stack,item)
    elif ch==2:
        Pop(Stack)
        if Stack==[]:
            print("Underflow! the stack is empty")
        else:
            print("Popped item is",item)
    else:
        for i in range(len(Stack)-1,-1,-1):
            print(Stack[i])

        
