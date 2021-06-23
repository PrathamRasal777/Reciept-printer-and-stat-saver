print("\t\t\t\t\t\t\t\t\t* WELCOME TO MY KIRANA STORE *")
f=open("kirana.txt","a")
w=input("sir/mam please enter your name : ")
f.write("\nCUSTOMER NAME: ")
f.write(w)


sum=0
while(True):
    y=(input("enter the name of product : "))
    if y=="q":
        break;
    f.write("\n")
    f.write(y+" =")
    n=(input("enter the rate of the metioned  product or press q to quit: "))
    #f.write("\n")
    f.write(f" {n} Rs")
    #f.write("{} {} ".format(y,n)+"=")
    if(n!="q"):
        try:
            sum=sum+int(n)
        except ValueError as e:
            print()
            print("WRONG INPUT OF N: ",e)
            print("RE-ENTER THE PREVIOUS PRODUCT BELOW")
            print()
    else:
        break


print(f"\nTHANKS FOR VISITING !!!\nYOUR TOTAL BILL IS : {sum} Rs/- only....")
f.write(f"\nTOTAL BILL : {sum} Rs/- only")
f.write("\nTHANKS FOR VISITING. HAVE A NICE DAY!!!!")
f.write("\n""______*****________")
f.close()
