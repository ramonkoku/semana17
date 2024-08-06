# main.py
from pessoa import Pessoa

nome = str(input('Digite o nome: '))
idade = int(input('Digite a idade: '))

pessoa1 = Pessoa(nome, idade)

print(f'Seu ano de nascimento é: {pessoa1.calcular_ano()}')
