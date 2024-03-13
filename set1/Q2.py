'''The given code of a password generator takes in five arguments:
1. Size of password
2. Minimum number of capital letters required
3. Minimum number of small letters required
4. Minimum number of digits required
5. Minimum number of required
Ensure the password returned fits the requirements'''
import random
def password(size,l):
    pw=""
    for i in range(l[0]):
        ch=random.randint(59,62)
        pw=pw+chr(ch)
    for i in range(l[1]):
        ch=random.randint(65,90)
        pw=pw+chr(ch)
    for i in range(l[2]):
        ch=random.randint(1,9)
        pw=pw+str(ch)
    for i in range(l[3]):
        ch1=random.randint(33,47)
        ch2=random.randint(58,64)
        ch3=random.randint(91,96)
        ch4=random.randint(123,126)
        l=[ch1,ch2,ch3,ch4]
        ch=random.randint(0,3)
        pw=pw+chr(l[ch])
    while len(pw)>size:
        k=random.randint(1,4)
        if k==1:
                ch=random.randint(33,47)
                pw=pw+chr(ch)
        elif k==2:
                ch=random.randint(18,122)
                pw=pw+chr(ch)
        elif k==3:
                ch=random.randint(1,9)
                pw=pw+str(ch)
        else:
                ch1=random.randint(33,47)
                ch2=random.randint(58,64)
                ch3=random.randint(91,96)
                ch4=random.randint(123,126)
                l=[ch1,ch2,ch3,ch4]
                ch=random.randint(0,3)
                pw=pw+chr(l[ch])
    return pw

def arrangement(pw):
    k=[]
    output=""
    while len(k)<len(pw):
        t=random.randint(0,len(pw)-1)
        if t not in k:
            k.append(t)
            output=output+pw[t]
    return output
        
def main():
    size=int(input("Enter the size of password required:"))
    cap=int(input("Enter minimum number of capital letters required:"))
    small=int(input("Enter minimum number of small letters required:"))
    digits=int(input("Enter minimum number of digits required:"))
    special=int(input("Enter minimum number of special characters required:"))
    l=[cap,small,digits,special]
    if cap+small+digits+special<=size:
        pw=password(size,l)
        print(pw)
        print(arrangement(pw))
        if(len(arrangement(pw))!=size):
            print("Size does not match")
    else:
        print("Invalid parameters")
if __name__=="__main__":
    main()
   