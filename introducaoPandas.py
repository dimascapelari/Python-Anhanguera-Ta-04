import pandas as pd

lista_nomes = 'Dimas Mariana Lulu'.split()

pd.DataFrame(lista_nomes, columns=['nome'])

print(pd.DataFrame(lista_nomes, columns=['nome']))
