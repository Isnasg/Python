side = float(input("Введите длину стороны квадрата: "))

perimeter = round(4 * side, 2)
area = round(side ** 2, 2)
diagonal = round((side ** 2 + side ** 2) ** 0.5, 2)

print(f"Периметр квадрата: {perimeter}")
print(f"Площадь квадрата: {area}")
print(f"Диагональ квадрата: {diagonal}")