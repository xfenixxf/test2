import math

# 1. Основные математические константы
print("=== Математические константы ===")
print(f"Число Пи (π): {math.pi}")
print(f"Число Эйлера (e): {math.e}")
print(f"Бесконечность: {math.inf}")
print()

# 2. Тригонометрические функции
print("=== Тригонометрические функции ===")
angle_deg = 60
angle_rad = math.radians(angle_deg)  # перевод градусов в радианы
print(f"Синус {angle_deg}°: {math.sin(angle_rad):.4f}")
print(f"Косинус {angle_deg}°: {math.cos(angle_rad):.4f}")
print(f"Тангенс {angle_deg}°: {math.tan(angle_rad):.4f}")
print()

# 3. Логарифмы и степени
print("=== Логарифмы и степени ===")
number = 100
print(f"Квадратный корень из {number}: {math.sqrt(number)}")
print(f"Натуральный логарифм ln({number}): {math.log(number):.4f}")
print(f"Десятичный логарифм log10({number}): {math.log10(number)}")
print(f"2 в степени 10: {math.pow(2, 10)}")
print()

# 4. Округление и модуль
print("=== Округление и модуль ===")
x = 5.7
y = -3.2
print(f"Округление вверх {x}: {math.ceil(x)}")
print(f"Округление вниз {x}: {math.floor(x)}")
print(f"Модуль (абсолютное значение) {y}: {math.fabs(y)}")
print()

# 5. Факториал и комбинаторика
print("=== Факториал и комбинаторика ===")
n = 5
print(f"Факториал {n}! = {math.factorial(n)}")
print(f"НОД чисел 48 и 18: {math.gcd(48, 18)}")
print()

# 6. Решение квадратного уравнения (демонстрация комплексного использования)
print("=== Решение квадратного уравнения ax² + bx + c = 0 ===")
a, b, c = 1, -5, 6
discriminant = b**2 - 4*a*c

if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Уравнение: {a}x² + {b}x + {c} = 0")
    print(f"Корни: x1 = {x1}, x2 = {x2}")
elif discriminant == 0:
    x = -b / (2*a)
    print(f"Уравнение: {a}x² + {b}x + {c} = 0")
    print(f"Один корень: x = {x}")
else:
    print(f"Уравнение: {a}x² + {b}x + {c} = 0")
    print("Действительных корней нет")