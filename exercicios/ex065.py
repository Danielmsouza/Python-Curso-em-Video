'''Program that takes several numbers and shows the average between them and which was the largest and smallest number entered. The program asks the user whether or not they want to continue typing the numbers'''
'''Programa que le varios numeros e mostra a media entre eles e qual foi o maior e o menor numero digitado. O programa pergunta ao usuario se quer continuar ou não a digitar os numeros'''

response = 'S'
sum =  quant = average = 0
while response in 'Ss':
    number = int(input('Enter the number: '))
    sum += number
    quant += 1
    if quant == 1:
        biggest = smallest =  number
    else:
        if number > biggest:
            biggest = number
        if number < smallest:
            smallest = number
    response = str(input('Do you want to continue? [S/N] ')).upper().strip()[0]
average = sum / quant
print(f'Do you typed {quant} numbers and the average were {average}')
print(f'The biggest value was {biggest} and the smallest was {smallest}')
