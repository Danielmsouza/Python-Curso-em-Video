'''Program that calculates the BMI and show your status'''
'''Programa que calcula o IMC e mostra o seu status'''

weight = float(input('What is the weight? '))
height = float(input('How tall is it? '))
bmi = weight / (height ** 2)
print(f'The BMI this person is {bmi:.1f}')
if bmi < 18.5 :
    print('You are underweight')
elif 18.5 <= bmi < 25:
    print('Congratulations, your weight is normal')
elif 25 <= bmi < 30:
    print('You are overweight')
elif 30 <= bmi < 40:
    print('You are obese')
elif bmi >= 40:
    print('You are morbidly obese')