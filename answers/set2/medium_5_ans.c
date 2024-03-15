#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  char username[20];
  char password[60]; // Increased password size (Error 1)

  // Get username with fgets, check return value (Error 2)
  printf("Enter username: ");
  if (fgets(username, sizeof(username), stdin) == NULL) {
    fprintf(stderr, "Error reading username\n");
    return 1;
  }

  // Remove trailing newline from username (security improvement)
  username[strcspn(username, "\n")] = '\0';

  // Get password with fgets, check return value (Error 2)
  printf("Enter password: ");
  if (fgets(password, sizeof(password), stdin) == NULL) {
    fprintf(stderr, "Error reading password\n");
    return 1;
  }

  // Remove trailing newline from password (security improvement)
  password[strcspn(password, "\n")] = '\0';

  // Secure password comparison (Error 3)
  const char* correct_password = "secret123"; // Use a constant string
  if (strcmp(password, correct_password) == 0) {
    printf("Welcome, %s\n", username);
  } else {
    printf("Incorrect password.\n");
  }

  int num_elements;

  // Get number of elements with scanf (Error 4)
  printf("Enter the number of elements for an array: ");
  if (scanf("%d", &num_elements) != 1) {
    fprintf(stderr, "Error reading number of elements\n");
    return 1;
  }

  // Allocate memory and check for allocation failure (improved memory management)
  int* arr = (int*)malloc(sizeof(int) * num_elements);
  if (arr == NULL) {
    fprintf(stderr, "Memory allocation failed\n");
    return 1;
  }

  // Get array elements with scanf (Error 5)
  for (int i = 0; i < num_elements; i++) {
    printf("Enter element %d: ", i + 1);
    if (scanf("%d", &arr[i]) != 1) {
      fprintf(stderr, "Error reading element %d\n", i + 1);
      break; // Exit loop on error
    }
  }

  // Free allocated memory to avoid leak (Error 5)
  free(arr);

  return 0;
}
