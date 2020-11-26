import math
def numbers(n: int):
    if n>=0:
        print(f"{n} ")
        return numbers(n-1)

def fib(n: int):
    if n >= 2:
        return fib(n-1)+fib(n-2)
    if n == 1:
        return 1
    return 0

def power(number: int, n: int):
    if n == 0:
        return 1
    return number*power(number, n-1)

def reverse(txt: str):
    if len(txt) == 1:
        return f'{txt}'
    return f'{txt[-1]}{reverse(txt[:len(txt)-1])}'

def factorial(n: int):
    if n == 0 or n == 1:
        return 1
    return n*factorial(n-1)

# def prime(n: int):

# def n_sums(n: int):

# def combinations(n: int):

def remove_duplicates(txt: str):
    if len(txt)==1:
        return f'{txt}'
    if txt[0]==txt[1]:
        return f'{remove_duplicates(txt[1:])}'
    return f'{txt[0]}{remove_duplicates(txt[1:])}'

# def balanced_parentheses(n: int):


# numbers(4)
# print(fib(11))
# print(power(2, 10))
# print(reverse("mars"))
# print(factorial(4))
