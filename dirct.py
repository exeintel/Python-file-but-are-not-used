import os

print("Hello, World!")

dircd = input("pls patch:")
os.chdir(dircd)
def dir0() : 
    name = input("Pls name dir : ")
    os.mkdir(name)
def rm() : 
    rname = input("Pls name remove dir : ")
    os.rmdir(rname)
def ren() : 
    rename = input("Pls name rename : ")
    ren = input("Pls name rename : ")
    os.rename(rename , ren )
    
print("===============")
print("ExEintel folder")
print("===============")
print("1 = create dir ")
print("2 = del dir ")
print("3 = rename dir ")
print("4 = in dir ")
call =int(input("pls nammeber : "))


if call == 1 : 
    dir0()
elif call == 2 : 
    rm()
elif call == 3 : 
    ren()
else : 
    print("Неправильный номер " , call )