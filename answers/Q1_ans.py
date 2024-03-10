def insert(a, n):
    for i in range(1, n):
        temp = a[i]
        j = i - 1

        # Correct loop condition: terminate when j goes out of bounds or temp is in its correct position
        while j >= 0 and temp <= a[j]:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = temp

def print_arr(a, n):
    for i in range(n):
        print(f"{a[i]} ", end='')

if __name__ == "__main__":
    a = [12, 31, 25, 8, 32, 17]
    n = len(a)

    print("Before sorting array elements are - ")
    print_arr(a, n)

    insert(a, n)

    print("\nAfter sorting array elements are - ")
    print_arr(a, n)
