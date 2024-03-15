#include <stdio.h>
void selection_sort(int arr[], int n) {

    int i, j, min_index;

  

    for (i = 0; i < n-1; i++) {

 

        min_index = i;

        for (j = i + 1; j < n; j++) {

            if (arr[j] < arr[min_index]) {

                min_index = j;

            }

        }

      

        int temp = arr[i];

        arr[i] = arr[min_index];

        arr[min_index] = temp;

    }

}

int main() {

    int my_array[] = {64, 25, 12, 22, 11};

    int n = sizeof(my_array) / sizeof(my_array[0]);

    

    selection_sort(my_array, n);

   

    printf("Sorted array: ");

    for (int i = 0; i < n; i++) {

        printf("%d ", my_array[i]);

    }

    printf("\n");

    return 0;

}