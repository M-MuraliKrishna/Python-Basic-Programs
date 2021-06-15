# 7. Design a menu driven program to check whether the number is i)A perfect number or not ii)Armstrong number or not iii)Palindrome or not
def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return("is a Perfect Number" if sum == n else "is not a Perfect Number")
def armstrong_number(num):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
    return ("is an Armstrong number"if num == sum else "is not an Armstrong number")
def number_palindrome(num):
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    return("is a palindrome!" if(temp==rev) else "is Not a palindrome!")


def string_palindrome(string):
    return("is a palindrome" if(string==string[::-1]) else "Not a palindrome")


while True:
    print()
    print("\t\t\tMenu Driven Programs\t\n")
    print("\t1.Check Perfect Number or Not\t\t\t2.Check Armstrong Number or Not")
    print("\n\t\t\t\t\t5.Exit")
    print("\n\t3.Check Number is Palindrome or Not\t\t4.Check String is Palindrome or Not")
    choice=int(input("\n\tEnter Your Choice:"))
    if choice==1:   
        num1=int(input("\n\tEnter an Integer To Check Perfect Number or Not : "))
        print("\n\t{0}".format(num1),perfect_number(num1))
        input("\n\t")
    elif choice==2:
        num1=int(input("\n\tEnter an Integer To Check Armstrong Number or Not : "))
        print("\n\t{0}".format(num1),armstrong_number(num1))
        input("\n\t")
    elif choice==3:
        num1=int(input("\n\tEnter an Integer To Check Palindrome : "))
        print("\n\t{0}".format(num1),number_palindrome(num1))
        input("\n\t")
    elif choice==4:
        num1=str(input("\n\tEnter String To Check Palindrome or Not: "))
        print("\n\t{0}".format(num1),string_palindrome(num1))
        input("\n\t")
    elif choice==5:
        print("\n\t𝕋𝕙𝕒𝕟𝕜𝕤 𝔽𝕠𝕣 𝕌𝕤𝕚𝕟𝕘 𝕋𝕙𝕚𝕤 ℙ𝕣𝕠𝕘𝕣𝕒𝕞 ❤")
        input("\n\t𝓟𝓻𝓮𝓼𝓼 𝓔𝓷𝓽𝓮𝓻 𝓚𝓮𝔂 𝓣𝓸 𝓔𝔁𝓲𝓽")
        exit("\n\t")
    else:
        print("\n\t𝕆𝕡𝕡𝕤! 𝕐𝕠𝕦 ℍ𝕒𝕧𝕖 𝔼𝕟𝕥𝕖𝕣𝕖𝕕 𝕎𝕣𝕠𝕟𝕘 𝕆𝕡𝕥𝕚𝕠𝕟! 𝕋𝕣𝕪 𝔸𝕘𝕒𝕚𝕟")