#Question 1

#program to accept the amount and the desired option,whether to convert the amount to word representation or to USD currency

import math

    #Lists

ones =["","One", "Two", "Three","Four", "Five", "Six", "Seven","Eight", "Nine"]                                         #List 1 (1,2,3,....)

tens=["","","Twenty", "Thirty", "Forty","Fifty", "Sixty", "Seventy", "Eighty","Ninety"]                                 #list 2 (20,30,40,....)

teens=["Ten", "Eleven", "Twelve","Thirteen", "Fourteen","Fifteen","Sixteen", "Seventeen", "Eighteen","Nineteen"]        #List 3 (10,11,12,....)


    #Get User Input

amu=int(input("Please Enter the Amount:"))

    #Process Convert Amount to USD

u=amu / 200
ceil_value = math.ceil(u)

if amu>=99999:
    print()

else:
    
    a=[0,0,0,0,0]
    i=0
    while amu>0:
        a[i]=amu%10
        i+=1
        amu=amu//10
    n=""
   
    
    if a[4]!=0:
        if(a[4]==1):
            n+=teens[a[3]]+ " Thousand "
        else:
            n +=tens[a[4]] +" "+ ones[a[3]]+ " Thousand "
    else:
        if a[3]!=0:
            n+ones[a[3]]+" Thousand "
    if a[2]!=0:
        n += ones[a[2]] +" Hundred and "
    if a[1] !=0:
        if(a[1] == 1):
            n+= teens[a[0]]
        else:
            n+= tens[a[1]] +" "+ones[a[0]]
    else:
        if a[0] !=0:
            n+= ones[a[0]]
    #Get User Input    
print("(To convert to word representation enter W, to convert to USD currency enter C)")
fur = input("Please enter your Option: ")

if fur == 'W' or fur == 'w':
    print(n)    #Out Put convert amount to word represent
else:
    print("Result:USD",ceil_value)      #Out Put convert amount to USD Currency
