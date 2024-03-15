n = int(input("Enter a number :"))

a = 0
b = 1
print(a)
print(b)
list1 = [0, 1]
for i in range(n-2):
    c = a+b
    a = b
    b = c
    print(c)
    list1.append(c)

print(list1)

list2 = []
for j in list1:
    k = j*j
    list2.append(k)

print(list2)

#printing the odd elements
print("Odd numbers ")
for m in list1:
  if m % 2 != 0:
    print(m)


print("Even numbers ")
for m in list1:
  if m % 2 == 0:
    print(m)
    
    
#fibonacchi