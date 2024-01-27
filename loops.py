
print('\n' +'-'*10 + ' Estrutura de Repetição ' +'-'*10 +'\n')

# A função range() em Python gera uma sequência de números. 
# Por padrão, a sequência começa em 0, aumenta em 1 
# e termina antes do número especificado.

print('\n Contagem Regressiva \n')

for c in range(6, 0, -1):
    print(c)
    
print('\n Loop "For In" em "Range" \n')

# Itera de 1 ate 5 e ignora o ultimo valor (6)
for c in range(1,6):
    print(c)

print('\n Loop Numbers de 1 até 9 \n')

# Adiciona 10 numeros, começando no 1 e ignorando o ultimo numero

numbers = range(1,10)

for i in numbers:
    print(i)



