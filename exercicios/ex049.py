'''Upgrade ex009 multiplication table'''
'''Melhorando o ex009 de tabuada'''

number = int(input('Enter the number to see your multiplication table: '))
for c in range(0, 11):
    print(f'{number} x {c} = {number * c}')
    