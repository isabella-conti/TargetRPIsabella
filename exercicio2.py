'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.



IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
'''

n = int(input("Digite um número para verificar se ele pertence a sequência de Fibonacci: "))


anterior, atual = 0, 1

if n == 0 or n == 1:
    pertence = True
else:
    pertence = False
    while atual < n:
        anterior, atual = atual, anterior + atual
        if atual == n:
            pertence = True
            break


if pertence:
    print(f"O número {n} pertence à sequência de Fibonacci.")
else:
    print(f"O número {n} não pertence à sequência de Fibonacci.")