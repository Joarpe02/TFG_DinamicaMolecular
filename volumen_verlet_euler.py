import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
dt = 0.02                   # paso de tiempo
tend = 20                   # tiempo de finalización de la simulación
n = int(tend / dt)          # números de iteraciones en la simulación 
x0, v0 = 0.0, 1.0           # posición y velocidades iniciales
k, m = 1.0, 1.0             # constante de boltzmann y masa del cuerpo

# Vector de tiempos
tvec = np.linspace(0, tend, n)

# Algoritmo de Verlet
x_verlet = np.zeros(n)      # vector de posición
v_verlet = np.zeros(n)      # vector de velocidad
x_verlet[0] = x0            # posición inicial
v_verlet[0] = v0            # velocidad inicial
x_prev = x0 - v0 * dt + 0.5 * (-k * x0 / m) * dt**2         # x(-dt) 

# Integración con Verlet (posición)
for i in range(0, n - 1):
    force = -k * x_verlet[i]
    x_next = 2 * x_verlet[i] - x_prev + (dt**2 / m) * force
    x_prev = x_verlet[i]
    x_verlet[i + 1] = x_next

# Cálculo de velocidades con Verlet
for i in range(1, n - 1):
    v_verlet[i] = (x_verlet[i + 1] - x_verlet[i - 1]) / (2 * dt)

# Recorte para espacio de fases, ya que v[n] no se calcula
x_verlet_cut = x_verlet[:-1]
v_verlet_cut = v_verlet[:-1]

# Algoritmo de Euler
x_euler = np.zeros(n)       # vector de posición
v_euler = np.zeros(n)       # vector de velocidad
x_euler[0] = x0             # posición inicial
v_euler[0] = v0             # velocidad inicial

# Cálculo de posiciones y velocidades
for i in range(n - 1):
    x_euler[i + 1] = x_euler[i] + v_euler[i] * dt
    v_euler[i + 1] = v_euler[i] - k * x_euler[i] * dt

# Solución exacta
x_exact = v0 * np.sin(tvec) + x0 * np.cos(tvec)

# Gráfica conjunta del algoritmo de Verlet
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Posición
ax1.plot(tvec, x_verlet, label='Verlet', linewidth=2)
ax1.plot(tvec, x_exact, '--', label='Exacta', linewidth=2)
ax1.set_title(f"Algoritmo de Verlet (dt = {dt})")
ax1.set_xlabel("Tiempo")
ax1.set_ylabel("Posición")
ax1.legend()
ax1.grid(True)

# Espacio de fases
ax2.plot(x_verlet_cut, v_verlet_cut, color='tab:blue')
ax2.set_xlabel("Posición")
ax2.set_ylabel("Momento")
ax2.set_title("Verlet - Espacio de fases")
ax2.axis("equal")
ax2.grid(True)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

# Gráfica conjunta del algoritmo de Euler
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Posición
ax1.plot(tvec, x_euler, label='Euler', linewidth=2)
ax1.plot(tvec, x_exact, '--', label='Exacta', linewidth=2)
ax1.set_title(f"Algoritmo de Euler (dt = {dt})")
ax1.set_xlabel("Tiempo")
ax1.set_ylabel("Posición")
ax1.legend()
ax1.grid(True)

# Espacio de fases
ax2.plot(x_euler, v_euler, color='tab:red')
ax2.set_xlabel("Posición")
ax2.set_ylabel("Momento")
ax2.set_title("Euler - Espacio de fases")
ax2.axis("equal")
ax2.grid(True)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()