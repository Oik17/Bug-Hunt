def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])

    return fib_sequence

try:
    num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
except ValueError:
    num_terms = 5

result = fibonacci(num_terms)

print(f"\nFibonacci sequence with {num_terms} terms: {result}")
