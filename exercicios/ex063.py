'''Program that read a number and displays the first elements of the Fibonacci sequence'''
'''Programa que le um numero e mostre os primeiros elementos da sequencia de Fibonacci'''

n = int(input('How many terms do you want show? '))
t1 = 0
t2 = 1
print(f'{t1} > {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' > {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' > The end')