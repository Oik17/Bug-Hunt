def fibonacci(n):
    fib_sequence = [0, 1]
    # Intentional logical error: Incorrect loop condition
    for i in range(0, n):
        # Intentional logical error: Incorrect Fibonacci sequence calculation
        fib_sequence.append(fib_sequence[i+1])

    print(fib_sequence) #print instead of return

# Intentional logical error: Incorrect user input handling
try:
    num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
except OverflowError:
  print("Input too large. Using default value (5)")
  num_terms = 5

result = fibonacci(num_terms)

# Intentional logical error: Incorrect message formatting
print(f"\nFibonacci sequence with {num_terms} terms: {result}")
