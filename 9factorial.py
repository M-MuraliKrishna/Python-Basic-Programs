# 9. Write a program to find the factorial of a number using functions and without using functions. Accept the input at runtime
import math
from math import factorial
def using_fun(n):
    global facto
    facto=1
    for i in range(n):
        facto+=facto*i
    return facto
def using_recursion(num1):
    if num1==1 or num1==0:
        return 1
    elif num1<0:
        return "Opps! Please Enter Positive Integer"
    else:
        return(num1*using_recursion(num1-1))
def using_method(num):
    if num<0:
        return "Opps! Please Enter Positive Integer"
    else:
        return factorial(num)
while True:
    print()
    print("\t\t\tFinding Factorial of Given Number\t\n")
    print("\t1.Find Using Without Function\t\t2.Find Using Function")
    print("\n\t\t\t\t5.Exit\n")
    print("\t3.Find Using Recursion\t\t4.Find Using Method")
    choice=int(input("\n\tEnter Your Choice:"))
    if choice==1:
        fact=1
        num1=int(input("\n\tEnter Any Number For Factorial:"))
        for i in range(num1):
            fact=fact+fact*i
        print("\n\tFactorial of {0} is =".format(num1),fact)
        input("\n\t")
    elif choice==2:
        n=int(input("\n\tEnter Any Number For Factorial:"))
        print("\n\tFactorial of {0} is =".format(n),using_fun(n))
        input("\n\t")
    elif choice==3:
        num=int(input("\n\tEnter Any Number For Factorial:"))
        print("\n\tFactorial of {0} is =".format(num),using_recursion(num))
        input("\n\t")
    elif choice==4:
        num=int(input("\n\tEnter Any Number For Factorial:"))
        print("\n\tFactorial of {0} is =".format(num),using_method(num))
        input("\n\t")
    elif choice==5:
        print("\n\t𝕋𝕙𝕒𝕟𝕜𝕤 𝔽𝕠𝕣 𝕌𝕤𝕚𝕟𝕘 𝕋𝕙𝕚𝕤 ℙ𝕣𝕠𝕘𝕣𝕒𝕞 ❤")
        input("\n\t𝓟𝓻𝓮𝓼𝓼 𝓔𝓷𝓽𝓮𝓻 𝓚𝓮𝔂 𝓣𝓸 𝓔𝔁𝓲𝓽")
        exit("\n\t")
    else:
        print("\n\t𝕆𝕡𝕡𝕤! 𝕐𝕠𝕦 ℍ𝕒𝕧𝕖 𝔼𝕟𝕥𝕖𝕣𝕖𝕕 𝕎𝕣𝕠𝕟𝕘 𝕆𝕡𝕥𝕚𝕠𝕟! 𝕋𝕣𝕪 𝔸𝕘𝕒𝕚𝕟")
        input("\n\t")