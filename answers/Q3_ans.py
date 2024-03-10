MAX_SIZE = 100
stack = [0] * MAX_SIZE
choice, n, top, x, i = 0, 0, -1, 0, 0

def push():
    global top, n, x
    if top >= n - 1:
        print("\n\tSTACK is over flow")
    else:
        print(" Enter a value to be pushed:")
        x = int(input())
        top += 1
        stack[top] = x

def pop():
    global top
    if top <= -1:
        print("\n\t Stack is underflow")
    else:
        print("\n\t The popped element is", stack[top])
        top -= 1

def display():
    global top, i
    if top >= 0:
        print("\n The elements in STACK \n")
        for i in range(top, -1, -1):
            print("\n", stack[i])
        print("\n Press Next Choice")
    else:
        print("\n The STACK is empty")

if __name__ == "__main__":
    print("\n Enter the size of STACK[MAX=%d]:" % MAX_SIZE)
    n = int(input())

    print("\n\t STACK OPERATIONS USING ARRAY")
    print("\n\t--------------------------------")
    print("\n\t 1.PUSH\n\t 2.POP\n\t 3.DISPLAY\n\t 4.EXIT")

    while choice != 4:
        print("\n Enter the Choice:")
        choice = int(input())

        if choice == 1:
            push()
        elif choice == 2:
            pop()
        elif choice == 3:
            display()
        elif choice == 4:
            print("\n\t EXIT POINT ")
        else:
            print("\n\t Please Enter a Valid Choice(1/2/3/4)")
