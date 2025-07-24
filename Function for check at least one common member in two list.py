#Write a PYTHON function that takes two lists and returns True if they have at least one common member.

def common():
    """Function that takes two lists and returns True if they have at least one common member"""

    m=int(input("Please enter how many list elements you want in list1: "))
    lst1=[]

    if(m<=0):
        print("Please enter a valid input")

    else:
        print("Input for list1")
        print("-"*20)
        for i in range(1, m+1):
            value1=input("Enter {} value: ".format(i))
            lst1.append(value1)

    print("-" * 50)
    print("List1 = {}".format(lst1))
    print("-" * 50)

    n=int(input("Please enter how many list elements you want in list2: "))
    lst2=[]

    if (n <= 0):
        print("Please enter a valid input")

    else:
        print("Input for list2")
        print("-" * 20)
        for j in range(1, n+1):
            value2 = input("Enter {} value: ".format(j))
            lst2.append(value2)

    print("-" * 50)
    print("List2 = {}".format(lst2))
    print("-" * 50)

    cnt = 0
    for ele in lst1:
        if(ele in lst2):
            print(ele)
            cnt+=1

    if (cnt>0):
        result="True"

    elif(cnt==0):
        result="False"

    print("Common element between {} & {} is \n {}".format(lst1, lst2, result))

common()
print("Program executed successfully")