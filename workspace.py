import math

def f(x, y):
    return x * math.sqrt(y)

def runge_kutta(x0, y0, xf, h):
    x = [x0]
    y = [y0]

    while x[-1] < xf:
        k1 = h * f(x[-1], y[-1])
        k2 = h * f(x[-1] + h/2.0, y[-1] + k1/2.0)
        k3 = h * f(x[-1] + h/2.0, y[-1] + k2/2.0)
        k4 = h * f(x[-1] + h, y[-1] + k3)
        y_next = y[-1] + (k1 + 2.0*k2 + 2.0*k3 + k4) / 6.0
        x_next = x[-1] + h

        x.append(x_next)
        y.append(y_next)

    return x, y

# Parámetros de la solución
x0 = 1.0        # Valor inicial de x
y0 = 4.0        # Valor inicial de y
xf = 1.6        # Valor final de x
h = 0.1         # Tamaño del paso

# Ejecutar el método Runge-Kutta
x, y = runge_kutta(x0, y0, xf, h)

# Encontrar el valor de y en x = 1.6
index = x.index(x[-1])
y_final = y[index]

# Imprimir resultado
print(f"El valor de y en x = {xf} es:", y_final)