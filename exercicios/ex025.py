'''Program that read the name and show if it has the word "silva" in the name'''
'''Programa que le o nome e mostra se tem a palavra "silva" no nome'''

name = str(input('Enter the name: ')).strip()
print(f'Has your name Silva? {"silva" in name.lower()}')