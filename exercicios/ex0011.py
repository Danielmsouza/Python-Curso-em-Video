'''Programm that reads the width and height of a wall and shows the area and amount of paint needed to paint the wall'''
'''Programa que lê a largura e a altura de uma parede e mostra a area e a quantidade de tinta necessaria para pintar a parede'''

width = float(input('Enter the width: '))
height = float(input('Enter the height: '))
area = width * height
paint_yield = float(input('what is the paint yield? '))
paint = area / paint_yield

print(f'A wall {width} meters wide and {height} meters high, it has an area of {area} square meters and are necessary {paint} liters of paint are needed to paint the wall.')