print("Welcome to mini calculator")


Var1= float(input("Your First Number:"))



Var2 = float(input("Your Second Numeber"))


xyz = str(input("Your Operation:"))



if xyz == "+":
    print(Var1 + Var2)



elif xyz == "-":
    print(Var1-Var2)



elif xyz == "*":
    print(Var1*Var2)



elif xyz == "/":
    
    if Var2==0:
       while Var2==0:
            print("Invalid Operation")
            Var2 = float(input("Enter Valid Number:"))
    print(Var1/Var2)       
    
else:
    print("Invalid Operator")
