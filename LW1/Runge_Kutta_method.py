# дифф.урав-е
def diff_eq(x):
    return 0.6 - 0.2 * x

#реализация метода Рунге-Кутты
def runge_kutta(x0, h, steps):
    x = x0
    for _ in range(steps):
        k1 = diff_eq(x)*h
        k2 = diff_eq(x + 0.5 * k1)*h
        k3 = diff_eq(x + 0.5 * k2)*h
        k4 = diff_eq(x + k3)*h
        x += (k1 + 2*k2 + 2*k3 + k4)/ 6
    return x

# Исходные данные
x0 = 0  # количество соли в момент t=0
h = 0.2  # шаг 
steps = 1000  # количество итераций

# Численное решение 
num_solution = runge_kutta(x0, h, steps)
print("Численное решение:", num_solution)