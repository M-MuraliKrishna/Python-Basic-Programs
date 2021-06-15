# 4. Illustrate the usage of files with the help of different functions defined on Files(such as write, read(demonstrate all four forms), 
# open, and close(use both the forms of closing a file)

while True:
     print("\n\t\t\t\tFile Handling")
     print("\n1.Create File\t\t2.Append Something in File")
     print("\n\t\t5.Exit")
     print("\n3.Erase File Data\t4.Read File")
     cho=int(input("\nEnter Your Choice:"))
     if cho==1:
# Python code to create a file
          file =open('LearnEverytime.txt','w')
          text=input("Write Something:")
          file.write(text)
          file.close()
          input("Do You Want To Continue! Press Enter")
     elif cho==2:
# Python code to illustrate append() mode
           file = open('LearnEverytime.txt','a')
           testAppend=input("Write Something for Append:")
           file.write(testAppend)
           file.close()
           print("Given Data Appended Successfully!")
           input("Do You Want To Continue! Press Enter")
     elif cho==3:
           file = open('LearnEverytime.txt','w')
           file.close()
           print("All File Data Has Been Erased Successfully!")
           input("Do You Want To Continue! Press Enter")
     elif cho==4:
# Python code to illustrate read()
           file = open("LearnEverytime.txt", "r")
           print (file.read())
           input("\nDo You Want To Continue! Press Enter")
     elif cho==5:
            print("Thank You For Using This Program \U0001F600")
            exit()
     else:
            print("Opps! You have Entered Wrong Option! Try Again")