#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char username[20];
    char password[6]; 
    printf("Enter username: ");
    fgets(username, sizeof(username), stdin);
    printf("Enter password: ");
    fgets(password, sizeof(password), stdin);

    char correct_password[] = "123\n"; 
    if (strcmp(password, correct_password) == 0) {
        printf("Welcome, %s\n", username);
    } else {
        printf("Incorrect password.\n");
    }

    int num_elements;

    printf("Enter the number of elements for an array: ");
    scanf("%d", &num_elements);
    int* arr = (int*)malloc(sizeof(int) * num_elements);

    for (int i = 0; i < num_elements; i++) {
        printf("Enter element %d: ", i + 1);
        scanf("%d", &arr[i]);
    }

    printf("Elements of the array: ");
    for (int i = 0; i <= num_elements; i++) { 
        printf("%d ", arr[i]);
    }

    return 0;
}
