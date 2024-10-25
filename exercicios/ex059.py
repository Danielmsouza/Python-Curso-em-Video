'''Program that reads 2 numbers and shows a menu and performs the requested operation'''
'''Programa que le 2 numeros e mostra um menu e realizar a operação solicitada'''

num1 = int(input('First number: '))
num2 = int(input('Second number: '))
option = 0
while option != 5 :
    print('''    [ 1 ] sum
        [ 2 ] multiply
        [ 3 ] bigger
        [ 4 ] new numbers
        [ 5 ] exit ''')
    option = int(input('>>>> What is your option? '))
    if option == 1:
        sum = num1 + num2
        print(f'The sum of {num1} and {num2} is {sum}')        
    elif option == 2:
        multiplication  = num1 * num2
        print(f'The multiplication  of {num1} and {num2} is {multiplication }') 
    elif option == 3:
        if num1 > num2:
            bigger = num1
        else:
            bigger = num2
        print(f'between the value {num1} and {num2} the bigger is {bigger}') 
    elif option == 4:
        print('Inform the values again:')
        num1 = int(input('First number: '))
        num2 = int(input('Second number: '))
    elif option == 5:
        print('finishing .....')
    else:
        print('Erro, try again')
    print('=-=' * 10)            
print('end of program')
