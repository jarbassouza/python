print('\n Estudando listas em Python \n')
print('-' *25)
print('\n Adicionando listas dentro de listas \n')

pessoa = list()
todos = []

pessoa.append('Jarbas')
pessoa.append('54')
# Adiciona a lista pessoa dentro da lista todos
todos.append(pessoa[:])

pessoa[0] = 'João'
pessoa[1] = 40

todos.append(pessoa)

print(todos)

for p in todos:
    print(f'nome: {p[0]} - idade: {p[1]}')
    
    