#include <stdio.h>

void bubbleSort(int arr[], int n) {  // Error: incorrect inner loop condition
  int i, j, temp;
  for (i = 0; i < n - 1; i++) {
    for (j = 0; j < n; j++) {  // This will lead to unnecessary passes
      if (arr[j] > arr[j + 1]) {
        temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
}

void printArr(int a[], int n) {
  int i;
  for (i = 0; i < n; i++)
    printf("%d ", a[i]);
}

int main() {
  int arr[] = {64, 34, 25, 12, 22, 11, 90};
  int n = sizeof(arr) / sizeof(arr[0]);

  printf("Before sorting array elements are - \n");
  printArr(arr, n);

  bubbleSort(arr, n);

  printf("\nAfter sorting (potentially incorrect) array elements are - \n");
  printArr(arr, n);

  return 0;
}
