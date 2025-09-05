# дифф.урав-е
def diff_eq(x):
    return 0.6 - 0.2 * x

#реализация метода Эйлера
def euler_method(x0, h, steps):
    x = x0
    for _ in range(steps):
        x += diff_eq(x) * h
    return x

# Исходные данные
x0 = 0  # количество соли в момент t=0
h = 0.2  # шаг 
steps = 1000  # количество итераций

# Численное решение
num_solution = euler_method(x0, h, steps)
print("Численное решение:", num_solution)

