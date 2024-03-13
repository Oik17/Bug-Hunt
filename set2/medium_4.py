
n = int(input("Enter a number :"))

a = 0
b = 1
for i in range(n):
    list1 = []
    c = a+b
    b = c
    a = b
    print(c)
    list1.append(c)

    print(list1)

for j in list1:
    list2 = []
    k = j*j
    list2.append(k)

print(list2)

print("Odd numbers ")
for m in list1:
  if m % 2 == 0:
    print(m)
  else:
     print(m)

print("Even numbers ")
for m in list1:
  if m % 2 != 0:
    print(list1)