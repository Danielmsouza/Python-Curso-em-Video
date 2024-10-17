'''Program that reads a sentence and says whether it is a palindrome, disregarding spaces'''
'''Programa que le uma frase e diga se ela é um palindromo, desconsiderando os espaços'''

phrase = str(input('Enter the phrase: ')).strip().upper()
words = phrase.split()
join = ''.join(words)
reverse = ''
for letter in range(len(join) - 1, -1, -1):
    reverse += join[letter]
if reverse == join:
    print('It is a palindrome! ')
else:
    print('It is not a palindrome!')