
from vectos_operations.app import Vector

Version 1
x = int(input("Inserte el valor de x:  "))
y = int(input("Inserte el valor de y:  "))

vector = Vector(x, y)
print(vector.magnitude())


# Version 2

first_vector_arr = input(
    "Inserte las coordenadas del primer vector:  ").split(",")
second_vector_arr = input(
    "Inserte las coordenadas del segundo vector:  ").split(",")

first_vector = Vector(int(first_vector_arr[0]), int(first_vector_arr[1]))
second_vector = Vector(int(second_vector_arr[0]), int(second_vector_arr[1]))

print('Dot point is:', first_vector.dot_product(second_vector))

# Version 3.0.0

print('\nAngle between: ', first_vector.find_angle(second_vector))
