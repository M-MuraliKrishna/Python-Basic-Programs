# 8. Show the different operations defined on Lists, Tuples and Dictionaries
def list_operation():
    lst=[66,4,22,2222,33,3]
    while True:
        print()
        print("\t\t\tWelcome To List")
        print("\n\t1.Insert \t\t\t2.Append\n\n\t3.Remove\t\t\t4.Pop\n\n\t5.Reverse\t\t\t6.Sort List")
        print("\n\t7.Display List\t\t\t8.Update Value\n\n\t9.Clear all Data\t\t10.Go to Dictonary Operation")
        print("\n\t11.Go to Tuple Operation\t12.Exit")
        choice=int(input("\n\tEnter Your Choice:"))
        if choice==1:
            pos=int(input("\n\tEnter Position of Element to be Insert:"))
            ele=int(input("\n\tEnter Element to be Insert:"))
            lst.insert(pos,ele)
            print("\n\tInsert Operation successful")
            print("\n\tEelement {0} is Inserted at Position {1}".format(ele,pos))
            print("\n\tList Elements are:",lst)
            input("\n\t")
        elif choice==2:
            a_ele=int(input("\n\tEnter Element to be Append:"))
            lst.append(a_ele)
            print("\n\tAppend Operation successful")
            print("\n\tEelement {0} is Appended at the End of List".format(a_ele))
            print("\n\tList Elements are:",lst)
            input("\n\t")
        elif choice==3:
            r_ele=int(input("\n\tEnter Element to be Removed from List:"))
            if r_ele in lst:
                lst.remove(r_ele)
                print("\n\tRemove Operation Successful")
                print("\n\tEelement {0} is Removed From List".format(r_ele))
            else:
                print("\n\tElement {0} is Not Avilable in The List".format(r_ele))
                print("\n\tOpps! Remove Operation Failed!")
            input("\n\t")
        elif choice==4:
            if not lst:
                print("\n\tPop Operation is Failed")
                input("\n\tOpps! List is Empty!")
            else:
                print("\n\tElement",lst.pop(),"is Poped From List")
                print("\n\tPop Operation is Successful")
            input("\n\t")
        elif choice==5:
            if not lst:
                print("\n\tReverse Operation is Failed")
                input("\n\tOpps! List is Empty!")
            else:
                print("\n\tBefore Reverse list elements are:",lst)
                lst.reverse()
                print("\n\tAfter Reverse list elements are:",lst)
                print("\n\tReverse Operation is Successful")
            input("\n\t")
        elif choice==6:
            if not lst:
                print("\n\tSort Operation is Failed")
                input("\n\tOpps! List is Empty!")
            else:
                print("\n\tBefore Sort list elements are:",lst)
                lst.sort()
                print("\n\tAfter Sort list elements are:",lst)
                print("\n\tSort Operation is Successful")
            input("\n\t")
        elif choice==7:
            print("\n\tList Elements are:",lst)
            input("\n\t")
        elif choice==8:
            if not lst:
                print("\n\tUpdate Operation is Failed")
                print("\n\tOpps! List is Empty!")
            else:
                p_el=int(input("\n\tEnter The position of element to be update:"))
                u_ele=int(input("\n\tEnter Element to be update at Position {0}:".format(p_el)))
                if p_el<len(lst):
                    print("\n\tBefore Update list elements are:",lst)
                    lst[p_el]=u_ele
                    print("\n\tAfter update. list elements are:",lst)
                    print("\n\tUpdate Operation is Successful")
                else:
                    print("\n\tOpps!Index does not exixts!")
            input("\n\t")
        elif choice==9:
            if not lst:
                print("\n\tClear Operation is Failed")
                input("\n\tOpps! List is Empty!")
            else:
                print("\n\tAre You Sure!You Want To Delete All Element From List!")
                clr=input("\n\tPlease Connform  with [y/n]:")
                if clr=="Y" or clr=="y":
                    lst.clear()
                    print("\n\tSuccess! All Element Has Been Deleted From List")     
            input("\n\t")
        elif choice==10:
            print("\n\tYou are Redirecting to Dictonary Opeartion")
            input("\n\tPress Enter To Go to Dictonary Operation")
            Dict_operation()
        elif choice==11:
            print("\n\tYou are Redirecting to Tuple Opeartion")
            input("\n\tPress Enter To Go to Tuple Operation")
            Tuple_operation()
        elif choice==12:
            print("\n\t𝕋𝕙𝕒𝕟𝕜𝕤 𝔽𝕠𝕣 𝕌𝕤𝕚𝕟𝕘 𝕋𝕙𝕚𝕤 ℙ𝕣𝕠𝕘𝕣𝕒𝕞 ❤")
            input("\n\t𝓟𝓻𝓮𝓼𝓼 𝓔𝓷𝓽𝓮𝓻 𝓚𝓮𝔂 𝓣𝓸 𝓔𝔁𝓲𝓽")
            exit("\n\t")
        else:
            print("\n\t𝕆𝕡𝕡𝕤! 𝕐𝕠𝕦 ℍ𝕒𝕧𝕖 𝔼𝕟𝕥𝕖𝕣𝕖𝕕 𝕎𝕣𝕠𝕟𝕘 𝕆𝕡𝕥𝕚𝕠𝕟! 𝕋𝕣𝕪 𝔸𝕘𝕒𝕚𝕟")
            input("\n\t")



def Dict_operation():
    dic={1:2,2:3,3:4}
    while True:
        print()
        print("\t\t\tWelcome To Dictonary")
        print("\n\t1.Insert \t\t\t2.Insert Multiple Value\n\n\t3.Pop\t\t\t\t4.PopItem\n\n\t5.Display\t\t\t6.Clear")
        print("\n\t7.Display Value Using Key\t8.Update Value\n\n\t9.Go to List Operation\t\t10.Go to Tuple Operation")
        print("\n\t11.Exit")
        choice=int(input("\n\tEnter Your Choice:"))
        if choice==1:
            i_k=int(input("\n\tEnter Key Element to be Insert:"))
            i_v=int(input("\n\tEnter Element to be Insert:"))
            dic.__setitem__(i_k,i_v)
            print("\n\tInsert Operation successful")
            print("\n\tEelement {0} is Inserted as key {1}".format(i_v,i_k))
            print("\n\tDictonary Elements are:",dic)
            input("\n\t")
        elif choice==2:
            n_ele=int(input("\n\tEnter No of Element:"))
            for i in range(n_ele):
                i_k=int(input("\n\tEnter Key Element to be Insert:"))
                i_v=int(input("\n\tEnter Element to be Insert:"))
                dic.__setitem__(i_k,i_v)
                print("\n\tInsert Operation successful")
                print("\n\tEelement {0} is Inserted as key {1}".format(i_v,i_k))
                print("\n\tDictonary Elements are:",dic)
            input("\n\t")
        elif choice==3:
            p_ele=int(input("\n\tEnter Key to be Pop from Dictonary:"))
            if p_ele in dic:
                dic.pop(p_ele)
                print("\n\tPop Operation Successful")
                print("\n\tKey {0} and value is Poped From Dictonary".format(p_ele))
            else:
                print("\n\tKey {0} is Not Avilable in The Dictonary".format(p_ele))
                print("\n\tOpps! Pop Operation Failed!")
            input("\n\t")
        elif choice==4:
            if not dic:
                print("\n\tPopItem Operation is Failed")
                input("\n\tOpps! Dictonary is Empty!")
            else:
                print("\n\tElement",dic.popitem(),"is Poped From Dictonary")
                print("\n\tPopItem Operation is Successful")
            input("\n\t")
        elif choice==5:
            print("\n\tDictonary Value are:",dic)
            input("\n\t")
        elif choice==6:
            if not dic:
                print("\n\tClear Operation is Failed")
                input("\n\tOpps! Dictonary is Empty!")
            else:
                print("\n\tAre You Sure!You Want To Delete All Element From Dictonary!")
                clr=input("\n\tPlease Connform  with [y/n]:")
                if clr=="Y" or clr=="y":
                    dic.clear()
                    print("\n\tSuccess! All Element Has Been Deleted From Dictonary")     
            input("\n\t")
        elif choice==7:
            av_key=int(input("\n\tEnter Key to be Display from Dictonary:"))
            if av_key in dic:
                k_v=dic.get(av_key)
                print("\n\tDisplay Operation Successful")
                print("\n\tKey {0}'s value is {1}".format(av_key,k_v))
            else:
                print("\n\tKey {0} is Not Avilable in The Dictonary".format(av_key))
                print("\n\tOpps! Display Operation Failed!")
            input("\n\t")
        elif choice==8:
            if not dic:
                print("\n\tUpdate Operation is Failed")
                print("\n\tOpps! Dictonary is Empty!")
            else:
                p_el=int(input("\n\tEnter The Key of element to be update:"))
                u_ele=int(input("\n\tEnter Element to be update as key {0}:".format(p_el)))
                if p_el in dic:
                    print("\n\tBefore Update dictonary elements are:",dic)
                    dic.__setitem__(p_el,u_ele)
                    print("\n\tAfter update. Dictonary elements are:",dic)
                    print("\n\tUpdate Operation is Successful")
                else:
                    print("\n\tOpps!Index does not exixts!")
            input("\n\t")
        elif choice==9:
            print("\n\tYou are Redirecting to List Opeartion")
            input("\n\tPress Enter To Go to List Operation")
            list_operation()
        elif choice==10:
            print("\n\tYou are Redirecting to Tuple Opeartion")
            input("\n\tPress Enter To Go to Tuple Operation")
            #Tuple_operation()
        elif choice==11:
            print("\n\t𝕋𝕙𝕒𝕟𝕜𝕤 𝔽𝕠𝕣 𝕌𝕤𝕚𝕟𝕘 𝕋𝕙𝕚𝕤 ℙ𝕣𝕠𝕘𝕣𝕒𝕞 ❤")
            input("\n\t𝓟𝓻𝓮𝓼𝓼 𝓔𝓷𝓽𝓮𝓻 𝓚𝓮𝔂 𝓣𝓸 𝓔𝔁𝓲𝓽")
            exit("\n\t")
        else:
            print("\n\t𝕆𝕡𝕡𝕤! 𝕐𝕠𝕦 ℍ𝕒𝕧𝕖 𝔼𝕟𝕥𝕖𝕣𝕖𝕕 𝕎𝕣𝕠𝕟𝕘 𝕆𝕡𝕥𝕚𝕠𝕟! 𝕋𝕣𝕪 𝔸𝕘𝕒𝕚𝕟")
            input("\n\t")

def Tuple_operation():
    tup=()
    while True:
        print()
        print("\t\t\tWelcome To Tuple")
        print("\n\t1.Insert \t\t\t2.Find Max Value\n\n\t3.Find Min Value\t\t4.Display")
        print("\n\t5.Go to List Operation\t\t6.Go to Dictonary Operation")
        print("\n\t7.Exit")
        choice=int(input("\n\tEnter Your Choice:"))
        if choice==1:
            lst=list(tup)
            tp=int(input("\n\tEnter The Element to be Insert:"))
            lst.append(tp)
            tup=tuple(lst)
            print("\n\tInsert Operation successful")
            print("\n\tEelement {0} is Inserted in Tuple".format(tp))
            print("\n\tDictonary Elements are:",tup)
            input("\n\t")
        elif choice==2:
            if not tup:
                print("\n\tMax Operation is Failed")
                input("\n\tOpps! Tuple is Empty!")
            else:
                print("\n\tMax Operation successful")
                print("\n\tMaximum Value is :",max(tup))
            input("\n\t")
        elif choice==3:
            if not tup:
                print("\n\tMin Operation is Failed")
                input("\n\tOpps! Tuple is Empty!")
            else:
                print("\n\tMinimum Operation successful")
                print("\n\tMinimum Value is :",min(tup))
            input("\n\t")
        elif choice==4:
            print("\n\tTuple Value are:",tup)
            input("\n\t")
        elif choice==5:
            print("\n\tYou are Redirecting to List Opeartion")
            input("\n\tPress Enter To Go to List Operation")
            list_operation()
        elif choice==6:
            print("\n\tYou are Redirecting to Dictonary Opeartion")
            input("\n\tPress Enter To Go to Dictonary Operation")
            Dict_operation()
        elif choice==7:
            print("\n\t𝕋𝕙𝕒𝕟𝕜𝕤 𝔽𝕠𝕣 𝕌𝕤𝕚𝕟𝕘 𝕋𝕙𝕚𝕤 ℙ𝕣𝕠𝕘𝕣𝕒𝕞 ❤")
            input("\n\t𝓟𝓻𝓮𝓼𝓼 𝓔𝓷𝓽𝓮𝓻 𝓚𝓮𝔂 𝓣𝓸 𝓔𝔁𝓲𝓽")
            exit("\n\t")
        else:
            print("\n\t𝕆𝕡𝕡𝕤! 𝕐𝕠𝕦 ℍ𝕒𝕧𝕖 𝔼𝕟𝕥𝕖𝕣𝕖𝕕 𝕎𝕣𝕠𝕟𝕘 𝕆𝕡𝕥𝕚𝕠𝕟! 𝕋𝕣𝕪 𝔸𝕘𝕒𝕚𝕟")
            input("\n\t")
while True:
    print()
    print("\t\t**********************************************************")
    print("\t\t*                                                        *")
    print("\t\t* ꧁༺Welcome To List Dictionary and Tuple Program ༻꧂ *")
    print("\t\t*                                                        *")
    print("\t\t**********************************************************")
    print("\t\t**********************************************************")
    print("\t\t*      1.List                         2.Dictonary        *")
    print("\t\t*                                                        *")
    print("\t\t*                                                        *")
    print("\t\t*                                                        *")
    print("\t\t*      3.Tuple                        4.Exit             *") 
    print("\t\t*                                                        *")
    print("\t\t*                                                        *")
    print("\t\t*                       ꧁༺ 𝓓𝓮𝓼𝓲𝓰𝓷𝓮𝓭 𝓑𝔂 𝓖𝓪𝓾𝓽𝓪𝓶 𝓒𝓸𝓭𝓮𝓼 ༻꧂*")
    print("\t\t**********************************************************")
    choice=int(input("\n\t\tEnter Your Choice:"))
    if choice==1:
            list_operation()
    elif choice==2:
            Dict_operation()
    elif choice==3:
            Tuple_operation()
    elif choice==4:
        print("\n\t\t𝕋𝕙𝕒𝕟𝕜𝕤 𝔽𝕠𝕣 𝕌𝕤𝕚𝕟𝕘 𝕋𝕙𝕚𝕤 ℙ𝕣𝕠𝕘𝕣𝕒𝕞 ❤")
        input("\n\t\t𝓟𝓻𝓮𝓼𝓼 𝓔𝓷𝓽𝓮𝓻 𝓚𝓮𝔂 𝓣𝓸 𝓔𝔁𝓲𝓽")
        exit("\n\t")
    else:
        print("\n\t\t𝕆𝕡𝕡𝕤! 𝕐𝕠𝕦 ℍ𝕒𝕧𝕖 𝔼𝕟𝕥𝕖𝕣𝕖𝕕 𝕎𝕣𝕠𝕟𝕘 𝕆𝕡𝕥𝕚𝕠𝕟! 𝕋𝕣𝕪 𝔸𝕘𝕒𝕚𝕟")
        input("\n\t\t")

# List_Tuple_Dict.py
# Displaying List_Tuple_Dict.py