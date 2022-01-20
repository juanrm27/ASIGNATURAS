def palindromo(cadena):
    cadena = cadena.replace(" ","")
    cadena = cadena.replace(",","")
    aux = cadena.upper()
    if aux == aux[::-1]:
        return True
    else:
        return False
    
print(palindromo('ana')) #true
print(palindromo('hola')) #false
print(palindromo('Ana')) #true
print(palindromo('sometamos o matemos')) #true
print(palindromo('No subas, abuson')) #true


