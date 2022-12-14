#  Напишите программу, которая принимает на вход координаты двух точек и находит 
#  расстояние между ними в 2D пространстве.
    # *Пример:*
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

xA = int(input('Input coordinate "X" 1-th point: '))
yA = int(input('Input coordinate "Y" 1-th point: '))
xB = int(input('Input coordinate "X" 2-th point: '))
yB = int(input('Input coordinate "Y" 1-th point: '))

print(f'A({xA},{yA}); B({xB},{yB}) -> ',end='')
from math import sqrt
distance = sqrt((xB-xA)**2 + (yB-yA)**2)
print(round(distance, 3))
