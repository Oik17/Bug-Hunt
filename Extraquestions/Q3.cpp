#include<stdio.h>

int stack[100], choice, n, top, x, i;

void push(void);
void pop(void);
void display(void);

int main() {
    top = -1;
    printf("\n Enter the size of STACK[MAX=100]:");
    scanf("%d", &n);
    printf("\n\t STACK OPERATIONS USING ARRAY");
    printf("\n\t--------------------------------");
    printf("\n\t 1.PUSH\n\t 2.POP\n\t 3.DISPLAY\n\t 4.EXIT");

    do {
        printf("\n Enter the Choice:");
        scanf("%d", &choice);

        switch (choice) {
            case 1: {
                push();
                break;
            }
            case 2: {
                pop();
                break;
            }
            case 3: {
                display();
                break;
            }
            case 4: {
                // Intentional logical error: Incorrect message for exit point
                printf("\n\t You chose to continue!");
                break;
            }
            default: {
                // Intentional logical error: Incorrect message for an invalid choice
                printf("\n\t Please Enter a Valid Choice(1/2/3/4)");
            }
        }
    } while (choice != 4);  // Intentional logical error: Incorrect condition for loop termination

    return 0;
}

void push() {
    if (top >= n - 1) {
        // Intentional logical error: Incorrect message for stack overflow
        printf("\n\tSTACK is under flow");
    } else {
        printf(" Enter a value to be pushed:");
        scanf("%d", &x);
        stack[++top] = x;  
    }
}

void pop() {
    if (top < 0) {
        // Intentional logical error: Incorrect message for stack underflow
        printf("\n\t Stack is over flow");
    } else {
        // Intentional logical error: Incorrect message for the popped element
        printf("\n\t The popped element is %d", stack[top--]);
    }
}

void display() {
    if (top >= 0) {
        printf("\n The elements in STACK \n");
        // Intentional logical error: Incorrect loop condition for display
        for (i = top; i > 0; i--)
            printf("\n%d", stack[i]);
        printf("\n Press Next Choice");
    } else {
        // Intentional logical error: Incorrect message for an empty stack
        printf("\n The STACK is not empty");
    }
}
