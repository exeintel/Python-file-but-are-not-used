# hi users
print("Hello, World!")
# programm 
name=input("pls yor name : ")
print("hi : " , name )
# info users 
print("Wellcom in ExEintel calt pro ")
num1=float(input("pls your nummber 1 :"))
num2=float(input("pls your nummber 2 :"))
# test zero error 
if num1 == 0 : 
    # programm zero
    print("programm no 0 in num1")
else: 
    # programm 
    print("1 = + ")
    print("2 = - ")
    print("3 = * ")
    print("4 = : ")
    print("5 = ^ ")
    cell=int(input("pls you operation :"))
    def p(): 
        print("result : " , num1 + num2)
    def m(): 
        print("result : " , num1 - num2)
    def u():
        print("result : " , num1 * num2)
    def d(): 
        print("result : " , num1 / num2)
    def s(): 
        print("result : " , num1 ** num2)
    if cell == 1 : 
        p()
    if cell == 2 : 
        m()
    if cell == 3 : 
        u()
    if cell == 4 : 
        d()
    if cell == 5 : 
        s()
print("goodbuy : " , name )
print("end programm ")
print("ExEintel calt pro ")
print(2025)