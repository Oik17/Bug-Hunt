def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def print_arr(a, n):
    for i in range(n):
        print(f"{a[i]} ", end='')

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    n = len(arr)

    print("Before sorting array elements are - ")
    print_arr(arr, n)

    bubble_sort(arr, n)

    print("\nAfter sorting array elements are - ")
    print_arr(arr, n)
