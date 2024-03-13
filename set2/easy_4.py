def fibonacci(n):
    if n <= 0:
        return [0]
    elif n == 1:
        return [1]
    else:
        fib_series = [0, 1]
        for i in range(2, n+1):
            fib_series.append(fib_series[i + 1] + fib_series[i + 2])
        return fib_series

def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, int(num/2) + 1):
            if num % i == 0:
                return False

def prime_fibonacci_sequence(n):
    fib_sequence = fibonacci(n)
    prime_fib_sequence = [ ]
    for num in fib_sequence:
        if is_prime(num):
            prime_fib_sequence.extend(num)
    print(prime_fib_sequence)

def main():
    n = int(input("Enter a number: "))
    prime_fib_seq = prime_fibonacci_sequence(n)
    print("Prime Fibonacci sequence up to", n, ":", prime_fib_seq)

if __name__ == "__main__":
    main()

