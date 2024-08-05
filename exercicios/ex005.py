'''Program that reads an integer and shows its successor and predecessor on the screen'''
'''Programa que le um numero inteiro e mostra na tela o seu sucessor e seu antecessor'''

num = int(input('Type the number: '))
predecessor = num - 1
sucessor = num + 1
print(f'Analyzing the number {num}, your predecessor is {predecessor} and your sucessor is {sucessor}.')
print(f'Analyzing the number {num}, your predecessor is {num-1} and your sucessor is {num+1}.')
