"""Write a program that asks the user to input 10
integers and then print the sum of the largest odd and smallest even numbers. If
no odd numbers are entered, it should print the sum of the digits of the 5th input
number. If no even numbers are entered, it should print the digit count of the 5th
input number."""
fifth = ""
sum = count = 0
even = odd = None
flag1 = flag2 = False
for i in range(10):
    n=int(input())
    if i==4:
        fifth=str(n)
    if n%2 == 0:
        flag1 = True
        if even is None or n<even:
            even=n
    else:
        flag2 = True
        if odd is None or n>odd:
            odd=n
if flag1 and flag2:
    print(odd+even)
elif flag1 and flag2==False:
    for i in fifth:
        sum += int(i)
    print(sum)
elif flag1==False and flag2:
    for i in fifth:
        count+=1
print(count)