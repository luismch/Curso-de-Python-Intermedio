# try, except

# def palindromo(string):
#     return string == string[::-1]

# try:
#     print(palindromo(1))
# except TypeError:
#     print("solo se pueden ingresar palabras")



#raise

# def palindromo(string):
#     try:
#         if len(string) == 0:
#             raise ValueError("no se puede ingresar una cadena vacia")
#         return string == string[::-1]
#     except ValueError as ve:
#         print(ve)
#         return False

# try:
#     print(palindromo(""))
# except TypeError:
#     print("solo se pueden ingresar palabras")



#finally


# try:
#     f = open( "archivo.txt")
#     #hacer cualquier cosa con nuestro archivo
# finally:
#     f.close()


def divisors(num):
    divisors = []
    for i in range(1, num +1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    try:

        num = int(input("ingresa un numero: "))
        print(divisors(num))
        print("termino mi programa")
    except ValueError:
        print("debes ingresar un numero")
        
if __name__ == "__main__":
    run()