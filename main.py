from funcoes import somaDoisNumeros
import pyodbc
import pytube

numero = 0
texto = 'Lucas'
valor = 5.75
lista = ['Lucas', 'Kenedy','murilo', 'Katiri']
booleana = False
booleana = True
nula = None

texto = 5
Texto = 1

# if numero == 5:
#     print('é cinco')
# elif numero ==6:
#     print('é seis')
# else:
#     print('não é cinco nem seis')

while numero < 10:
    # print(numero)
    numero += 1

# for i in lista:
# for i in range(10):
# for i in range(len(lista)):
# for i,j in enumerate(lista):
#     print(i,j)

texto = 'Lucas'
# print(len(texto))
# print(texto.index('as'))
# if 'uc' in texto:
#     print('achou')


print(somaDoisNumeros(4,8))

texto = 'era uma vez, na betha, foi hoje'
a,b,c = texto.split(',')
# print(a)
# print(b)
# print(c)
empresa = 'betha'
texto = f'era uma vez, na {numero}, foi hoje'
# print(texto)
texto = 'era uma vez, na {}, foi hoje{}{}'.format(empresa,empresa,empresa)
# print(texto)

try:
    nova = texto /12
    print(nova)
except Exception as erro:
    print(f'deu erro {erro}')
finally:
    print('oi')

