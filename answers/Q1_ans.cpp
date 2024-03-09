#include <stdio.h>

void insert(int a[], int n) {
  for (int i = 1; i < n; i++) {
    int temp = a[i];
    int j = i - 1;

    /* Correct loop condition: terminate when j goes out of bounds or temp is in its correct position */
    while (j >= 0 && temp <= a[j]) {
      a[j + 1] = a[j];
      j--;
    }

    a[j + 1] = temp;
  }
}

void printArr(int a[], int n) {
  int i;
  for (i = 0; i < n; i++)
    printf("%d ", a[i]);
}

int main() {
  int a[] = {12, 31, 25, 8, 32, 17};
  int n = sizeof(a) / sizeof(a[0]);

  printf("Before sorting array elements are - \n");
  printArr(a, n);

  insert(a, n);

  printf("\nAfter sorting array elements are - \n");
  printArr(a, n);

  return 0;
}
