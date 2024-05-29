# 3. Gerador de Senhas
# Crie um gerador de senhas que possa gerar senhas aleatórias com base em critérios definidos pelo usuário, 
# como comprimento e tipos de caracteres (maiúsculas, minúsculas, números, símbolos).

import itertools
import random

# Verificador de números
def verifica_num(value):
    try:
        int(value) # tenta converter em Int
        return True
    except ValueError:
        return False

print('GERADOR DE SENHAS')
qtd = input('Quantos caracteres deseja que a senha tenha? ')

# Valida valor inteiro digitado
while qtd == '0' or verifica_num(qtd) == False:
    qtd = input('Valor inválido. Digite novamente: ')
qtd = int(qtd)

caracteres = 'qwertyuiopasdfghjklçzxcvbnm1234567890!@#$%&*()-_=+[{]}/?;:.>,<\|]'

def gerar_senha(qtd):
    for i in range(1, qtd+1):
        for perm in itertools.permutations(random.sample(caracteres, i)):
            senha = ''.join(perm)
    return senha

print('Senha gerada: ', gerar_senha(qtd))