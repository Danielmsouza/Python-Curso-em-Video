'''Program that reads 2 notes and calculates the average of the notes and displays a message according to the average'''
'''Programa que le 2 notas e calcula a media das notas e mostra uma mensagem de acordo com a media'''

note1 = float(input('Enter the first note: '))
note2 = float(input('Enter the second note: '))
average = (note1 + note2) / 2
print(f'The average of the notes {note1} and {note2} is {average}')
if 7 > average >= 5:
    print('recovering student')
elif average < 5:
    print('failed student')
else:
    print('approved student')