"""
Este programa vai mostrar Fizz para números divisiveis por 3
Buzz para números divisiveis apenas por 5 e
FizzBuzz para números divisiveis por 3 e 5
"""


def fizzBuzz(n) -> str:
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


print("\n".join(fizzBuzz(numero) for numero in range(1, 50)))
