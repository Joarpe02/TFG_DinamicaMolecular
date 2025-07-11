import numpy as np
import matplotlib.pyplot as plt

def verlet_simulation(ax, dt, t_end=20, k=1.0, m=1.0, x0=0.0, v0=1.0):
    n = int(t_end / dt)               # números de iteraciones en la simulación
    x = np.zeros(n)                   # vector de posición
    v = np.zeros(n)                   # vector de velocidad
    tvec = np.linspace(0, t_end, n)   # vector de tiempos

    # Condiciones iniciales
    x[0] = x0
    x_prev = x0 - v0 * dt + 0.5 * (-k * x0 / m) * dt**2         # x(-dt)

    # Integración con Verlet (posición)
    for i in range(0, n - 1):
        force = -k * x[i]
        x_next = 2 * x[i] - x_prev + (dt**2 / m) * force
        x_prev = x[i]
        x[i + 1] = x_next

    # Solución exacta
    x_exact = x0 * np.cos(tvec) + v0 * np.sin(tvec)

    # Gráfico
    ax.plot(tvec, x, label="Verlet")
    ax.plot(tvec, x_exact, '--', label="Exacta")
    ax.set_xlabel("Tiempo")
    ax.set_ylabel("Posición")
    ax.set_title(f"dt = {dt}")
    ax.legend()
    ax.grid(True)

# Crear una figura con 2 subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Ejecutar para dt = 0.02 y dt = 2
verlet_simulation(ax1, dt=0.02)
verlet_simulation(ax2, dt=2)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()