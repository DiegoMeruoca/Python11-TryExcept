"""Este programa utiliza o try except para fazer o tratamento
de erro, deste modo pode seguir seu funcionamento naturalmente"""
a = 10
b = 0
try:
    print(a / b)
except:
    print("Não podemos dividir por 0")
print("Continuação do programa")
