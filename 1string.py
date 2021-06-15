# 1. Demonstrate runtime reading of Strings. 
# i) Illustrate the concept of String Slicing. 
# ii) Also demonstrate a minimum of 5 functions defined on Strings

print("\n\t\t\t\tString Slicing\n")
String=input("Please Enter a String For String Slicing:")
# String=”Gautam’s Online Learning www.LearnEverytime.com”
s1 = slice(3)
s2 = slice(1, 5, 2)
s3 = slice(-1, -12, -2)
print("Your Given String Is:",String)
print("slice(3):",String[s1])
print("slice(1,5,2):",String[s2])
print("slice(-1,-12,-2):",String[s3])
print("String[:3]:",String[:3])
print("String[1:5:2]:",String[1:5:2])
print("String[-1:-12:-2]:",String[-1:-12:-2])
print("String[2:3]:",String[2:3])
print("String[2:-2]:",String[2:-2])
print("String[-2:5]:",String[-2:5])
print("String[-4:3:-2]:",String[-4:3:-1])
print("Reverse String:",String[::-1])
# 5 string Methods
print("\n\t\t\t\tString Slicing Methods\n")
print("String In Upper Case:",String.upper())
print("String In Lower Case:",String.lower())
print("StartWith Method:",String.startswith("www"))
print("StartWith Method:",String.endswith("com"))
print("StartWith Method:",String.split(","))
#If you are a beginer you can ignore rest of code
hellp=input("For More Information Type[y/n]:")
if hellp=="Y" or hellp=="y":
        print("Double Click On The Squeezed Test(408 lines).")
        print(help(str))
else:
        print("Have a Nice Day \U0001F600")