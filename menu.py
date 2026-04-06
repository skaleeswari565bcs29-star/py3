l=list(map(int,input("enter elements of list separated by using space:").split()))
while(1):
    print("\t\tMENU")
    print("1. max value")
    print("2. min value")
    print("3. slicing the list")
    print("4. occurence of an item")
    print("5. first occurence of an item")
    print("6. exit")
    choice =int(input("enter your choice:"))
    if choice==1:
        print("max value",max(l))
    elif choice==2:
        print("min value",min(l))
    elif choice==3:
        print("slicing the list")
        s=int(input("enter starting index:"))
        e=int(input("enter ending index:"))
        print("sliced list:",l[s:e])
    elif choice==4:
        item=int(input("enter item:"))
        print("occurence of an item",l.count(item))
    elif choice==5:
        item=int(input("enter item to be found:"))
        if item in l:
            print("first occurence of an item",l.index(item))
        else:
            print("item not found")
    elif choice==6:
          print("exit")
          break
    else:
        print("invalid choice")
