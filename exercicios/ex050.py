'''Program that reads 6 integers and displays the sum of only those that are even. If the value is odd, disregard it '''
'''Programa que le 6 numeros inteiros e mostre a soma apenas dos que forem pares. Se o valor for impar desconsidere'''

sum = 0
cont = 0
for c in range (1, 7):
    num = int(input(f'Enter the {c} value: '))
    if num % 2 == 0:
        sum += num
        cont += 1
print(f'You typed {cont} number pairs and the sum was {sum}')