# Рост амёбы ---
print("Рост амёбы (каждые 3 часа до 24 часов):")
ameba = 1
for time in range(3, 25, 3):
    ameba *= 2
    print(f"Через {time} часов: {ameba} клеток")

print("\nТаблица значений функции y = -0.5x + x:")
# Таблица значений ---
x_min = 1
x_max = 3
step = 0.5

print("x\t y")
x = x_min
while x <= x_max + 1e-8:
    y = -0.5 * x + x  # можно упростить до y = 0.5 * x
    print(f"{x:.1f}\t {y:.2f}")
    x += step
