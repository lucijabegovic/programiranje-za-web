def zbroji (a,b):
    rezultat = a + b
    print(rezultat)

def oduzmi (a,b):
    rezultat = a - b
    print(rezultat)

def pomnozi (a,b):
    rezultat = a * b
    print(rezultat)

def podjeli (a,b):
    rezultat = a / b
    print(rezultat)

a = int(input("unesi broj a: "))
b = int(input("unesi broj b: "))
o = input("odaberi matematicku operaciju + , - , *, /")

if o == "+":
    zbroji (a,b)

elif o == "-":
    oduzmi (a,b)

elif o == "*":
    pomnozi (a,b)
    
elif o == "/":
    podjeli (a,b)
