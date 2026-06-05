
print("Hello, World!")
print("Welcome")
num1=float(input("pls 1 nummber : "))
num2=float(input("pls 2 nummber : "))
if num1 == 0 : 
    print("no zero in nummber 1 ")
    print("end programm ")
else : 
    print("1 = +")
    print("2 = - ")
    print("3 = *")
    print("4 = :")
    call = int(input("pls nummber operation : "))
    def c() : 
        print(num1 + num2)
    def v() : 
        print(num1 - num2)
    def u() : 
        print(num1 * num2)
    def d() : 
        print(num1 / num2)
    if call == 1 : 
        c()
    if call == 2 : 
        v()
    if call == 3 : 
        u()
    if call == 4 : 
        d()
    print("end programm")