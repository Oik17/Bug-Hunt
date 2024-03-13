def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n):  # This will lead to unnecessary passes
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

def print_arr(a, n):
    for i in range(n):
        print(f"{a[i]} ", end='')

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    n = len(arr)

    print("Before sorting array elements are - ")
    print_arr(arr, n)

    bubble_sort(arr, n)

    print("\nAfter sorting (potentially incorrect) array elements are - ")
    print_arr(arr, n)
