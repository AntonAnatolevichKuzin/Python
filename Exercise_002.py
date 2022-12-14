#Напишите программу для. проверки истинности утверждения 
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('Enter X value: '))
y = int(input('Enter Y value: '))
z = int(input('Enter Z value: '))

result = not(x and y and z) == (not (x) or not (y) or not (z))

if result == True:
    print('True')
else:
    print('Not true')
