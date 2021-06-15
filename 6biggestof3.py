# 6. Write a program to find the biggest of three numbers

a=int(input("Enter The Value of X:"))
b=int(input("Enter The Value of y:"))
c=int(input("Enter The Value of z:"))
lst=[]
lst.append(a)
lst.append(b)
lst.append(c)
lst.sort(reverse=True)
print("Greatest Number is:",lst[0])