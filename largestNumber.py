#Print the largest number among the three numbers:
num1=int(input('Enter number1:'))
num2=int(input('Enter number2:'))
num3=int(input('Enter number3:'))

if(num1>=num2) and (num1>=num3):
    print('Num1 is the largest!')
elif(num2>=num1) and (num2>=num3):
    print('Num2 is the largest!')
else:
    print("Isnt it obvious?!")
