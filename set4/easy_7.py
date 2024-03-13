num = 29
flag = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(1, num,2):
        if (num % i) == 0:
            flag = True

    if flag:
        print(num, "is a prime number")  
    else:
        print(num, "is not a prime number")  


def compute_hcf(x, y):

    if y > x:
        s = y
    else:
        s = x
    for i in range(1, s):
        if((x % i == 0) and (y % i == 0)):  
            hcf=i

    return hcf

num1 = 54
num2 = 24

print("The H.C.F. is", compute_hcf(num1, num2))
