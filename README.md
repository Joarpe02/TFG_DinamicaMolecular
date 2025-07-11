# TFG_DinamicaMolecular
Este repositorio contiene los scripts implementados para apoyar la revisión bibliográfica realizada sobre la dinámica molecular.

Por un lado, el archivo sim_estabilidad_verlet.py simula el movimiento de un oscilador armónico mediante el algoritmo de Verlet para dos pasos de integración distintos, mostrando la influencia de dicho parámetro en la estabilidad del algoritmo.

Por otro lado, el archivo volumen_verlet_euler.py simula el movimiento de un oscilador armónico mediante el algoritmo de Verlet (simpléctico) y el de Euler (no simpléctico), mostrando cómo los algoritmos no simplécticos no conservan el volumen en el espacio de fases, luego no son estables, mientras que los simplécticos, sí.
