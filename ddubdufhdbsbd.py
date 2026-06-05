
print("Hello, World!")

call=input("Введите имя : ")

def hello(name) : 
    print("Привет " , name , "чем сейчас займемся ?")
    
def void() : 
    input=(" ")

print("1 = hello")
print("2 = close ")

xall=int(input("Пожайлуста ввелите номер операцыии : "))

if xall == 1 : 
    hello(call)
elif xall == 2 : 
    void()
else : 
    print("Неправелтный ввод ")
