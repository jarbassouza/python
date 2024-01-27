
# A função 'capitalize()' converte a primeira letra da linha para maiúsculo
# A função 'upper()' convete todo o texto para maiúsculo
# A função 'title()' As primeira letras das palavras em maiúsculo

print('Estudando Dicionarios Python')
print('-' *20)

pessoas = {'nome':'Jarbas', 'sexo':'M', 'idade': 54}

# del pessoas['sexo'] # Apaga o item sexo

pessoas ['nome'] = 'Jarbinhas' # Altera o nome
pessoas['peso'] = 65.8 # Adiciona o item peso no dicionario

for k, v in pessoas.items():
    print(f'{k} = {v}')
    
print('-' *30)

print('Colocando dicionarios dentro de listas')

brasil = [] # Declarando uma lista 'list()'
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil)

print(type(brasil)) # Lista é um tipo de classe

print(brasil[0]['uf']) # acessando os dados da lista

print('Copiando um dicionario')

estado = dict()
brasil = list()

for c in range(0,3):
    estado['Uf'] = str(input('Unidade Federativa:\n')).title()
    estado['Sigla'] = str(input('Sigla do Estado:\n')).upper()
    # Faz uma copia do estado para a lista Brasil
    brasil.append(estado.copy()) 
print(brasil)
for e in brasil:
        # print(e)
    for k, v in e.items():
        print(f'A Chave {k} tem o Valor {v}')