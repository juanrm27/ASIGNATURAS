class Spain():

    def __str__(self) -> str:
        return 'España'

    def capital(self):
        print('La capital de España es Madrid')
    def idioma(self):
        print('El idioma oficial es el Castellano')

class Portugal():

    def __str__(self) -> str:
        return 'Portugal'

    def capital(self):
        print('La capital de Portugal es Lisboa')
    def idioma(self):
        print('El idioma oficial es el Portugués')


class Aduana():
    def pasar(self, pais):
        print(f'Ahora estoy en {pais}')
        pais.capital()
        pais.idioma()


esp = Spain()
por = Portugal()

paises = [esp,por]

# for p in paises:
#     p.capital()
#     p.idioma()


audana = Aduana()    
for p in paises:
    audana.pasar(p)