'''Program that reads the weight of 5 people and shows which was the biggest and lowest weight'''
'''Programa que le o peso de 5 pessoas e mostre qual foi o maior e o menor peso'''

biggest = 0
lowest = 0
for person in range(1,6):
    weight = int(input(f'What is your weight? '))
    if person == 1:
        biggest = weight
        lowest = weight
    else:
        if weight > biggest:
            biggest = weight
        if weight < lowest:
            lowest = weight
print(f' The biggest weight was: {biggest}')
print(f' The lowest weight was: {lowest}')
