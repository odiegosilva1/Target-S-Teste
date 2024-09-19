    # Verifica se o número é menor que 0, que não faz parte da sequência
def pertence_fibonacci(n):
    if n < 0:
        return False
    
    # Inicializa os dois primeiros números da sequência
    a, b = 0, 1
    
    # Enquanto o segundo número da sequência for menor ou igual ao número informado
    while b < n:
        # Atualiza os números da sequência
        a, b = b, a + b
    
    # Verifica se o número informado é igual ao número atual da sequência
    return b == n

def main():
    try:
        # Solicita ao usuário que informe um número
        numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        return
    
    # Verifica se o número pertence à sequência de Fibonacci
    if pertence_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")

# Executa o programa
if __name__ == "__main__":
    main()
