# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

def is_fibonacci_number(number):
    a, b = 0, 1
    while b < number:
        a, b = b, a + b
    return b == number

try:
    input_number = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
    if is_fibonacci_number(input_number):
        print(f"{input_number} pertence à sequência de Fibonacci.")
    else:
        print(f"{input_number} não pertence à sequência de Fibonacci.")
except ValueError:
    print("Por favor, digite um número válido.")