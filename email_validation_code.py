email=input("Enter Your Email :") #g@g.in    g@g.com
k=0
j=0
d=0
if len(email)>=6:  #1
    if email[0].isalpha(): #2
        if ("@" in email) and (email.count("@")==1): #3
            if (email[-4]==".") ^ (email[-3]=="."): #4
                for i in email:
                    if i==i.isspace(): #5
                        k=1
                    elif i.isalpha():
                        if i==i.upper(): #5
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("wrong Email 5")
                else:
                    print("right Email")
            else:
                print("wrong Email 4")
        else:
            print("wrong Email 3")
    else:
        print("wrong Email 2 ")
else:
    print("wrong Email 1 ")

