#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num, *arr, i;
    scanf("%d", &num);
    arr = (int*) malloc(num * sizeof(int));
    for(i = 0; i < num; i++) {
        scanf("%d", arr + i);
    }

    int arr2[num];
    for(i = 0;i<num;i++)
    {
        arr2[i]=0;
    }
    
    for(i=0 ; i<num;i++)
    {
        arr2[i] = arr[num-1-i]; 
    }

    for(i = 0; i < num; i++)
    {
        printf("%d ", arr2[i]);
    }
    return 0;
}
