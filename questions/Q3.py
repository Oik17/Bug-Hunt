stack = [0] * 100
choice, n, top, x, i = 0, 0, 0, 0, 0

def push():
    global top, n, x
    if top >= n - 1:
        # Intentional logical error: Incorrect message for stack overflow
        print("\n\tSTACK is under flow")
    else:
        print(" Enter a value to be pushed:")
        x = int(input())
        top += 1
        stack[top] = x

def pop():
    global top
    if top < 0:
        # Intentional logical error: Incorrect message for stack underflow
        print("\n\t Stack is over flow")
    else:
        # Intentional logical error: Incorrect message for the popped element
        print("\n\t The popped element is", stack[top])
        top -= 1

def display():
    global top, i
    if top >= 0:
        print("\n The elements in STACK \n")
        # Intentional logical error: Incorrect loop condition for display
        for i in range(top, 0, -1):
            print("\n", stack[i])
        print("\n Press Next Choice")
    else:
        # Intentional logical error: Incorrect message for an empty stack
        print("\n The STACK is not empty")

if __name__ == "__main__":
    top = -1
    print("\n Enter the size of STACK[MAX=100]:")
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
            # Intentional logical error: Incorrect message for exit point
            print("\n\t You chose to continue!")
        else:
            # Intentional logical error: Incorrect message for an invalid choice
            print("\n\t Please Enter a Valid Choice(1/2/3/4)")
