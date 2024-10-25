# Função para verificar se um número pertence à sequência de Fibonacci
def is_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num or num == 0

# Número de entrada para verificação na sequência de Fibonacci
num = int(input("Digite um número para verificar se ele pertence à sequência de Fibonacci: "))

if is_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")

# Função para contar a letra "a" em uma string
def count_a_in_string(text):
    count = text.lower().count('a')
    return count

# Entrada da string para contagem de letras "a"
text = input("Digite uma string para verificar a presença da letra 'a': ")

count = count_a_in_string(text)
if count > 0:
    print(f"A letra 'a' ocorre {count} vezes na string.")
else:
    print("A letra 'a' não ocorre na string.")

# Loop corrigido para somar valores até o índice
INDICE = 12  # Variável para definir o limite
SOMA = 0     # Inicializa a soma em zero
K = 1        # Inicializa o contador em 1

# Estrutura de repetição para somar de 1 até o valor de INDICE
while K <= INDICE:
    SOMA += K  # Soma o valor de K à variável SOMA
    K += 1     # Incrementa K

# Exibe o resultado da soma final
print("O valor da soma é:", SOMA)

