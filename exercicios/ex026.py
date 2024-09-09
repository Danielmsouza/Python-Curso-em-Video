'''Program that counts how many times the letter "A" appears and what the first and last position is in which it appears'''
'''Programa que conta quantas vezes a letra "A" aparece e qual a primeira e ultima posição que ela aparece'''

phrase = str(input('Enter the phrase: ')).upper().strip()
print(f'The letter A appears {phrase.count("A")} times in this phrase.')
print(f'The first letter A appear in the position {phrase.find("A")+1}')
print(f'The last letter A appear in the position {phrase.rfind("A")+1}')
