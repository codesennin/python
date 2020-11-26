def zad1(a, b):
    return f"{a}. {b}"
# print(zad1("J","Kowalski"))

def zad2(a, b):
    return f"{a.capitalize()}. {b.capitalize()}"
# print(zad2("j","kowalski"))

def zad3(a, b, c):
    rok = a*100+b
    return rok-c
# print(zad3(20,20,19))

def zad4(a, b, foo):
    return foo(a[0], b)
# print(zad4("Jan","Kowalski", zad2))

def zad5(a, b):
    if a>=0 and b>0:
        return a/b
# print(zad5(2,4))

def zad6():
    a = 0
    while a<100:
        b = input("Podaj liczbe: ")
        if(a+int(b)>100):
            b = input("Ta liczba jest za duża, podaj mniejszą: ")
        a += int(b)
        print(f"a aktualnie wynosi: {a}")
# zad6()

def zad7(a):
    return tuple(a)
# print(zad7([1,2,4,7,123,64,21,42]))

def zad8():
    lista=[]
    a=input("Podaj wartość [koniec przerywa działanie programu]: ")
    while a!="koniec":
        lista.append(a)
        a=input("Podaj kolejną wartość [koniec przerywa działanie programu]: ")
    print(tuple(lista))
# zad8()

def zad9(a):
    dni=["poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela"]
    return dni[a-1]
# print(zad9(4))

def zad10(a):
    if a==a[::-1]:
        return True
    return False
print(zad10("level"))