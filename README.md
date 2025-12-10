# TFG_DinamicaMolecular
Este repositorio contiene los scripts implementados para apoyar la revisión bibliográfica realizada sobre la dinámica molecular.

Por un lado, el archivo sim_estabilidad_verlet.py simula el movimiento de un oscilador armónico mediante el algoritmo de Verlet para dos pasos de integración distintos, mostrando la influencia de dicho parámetro en la estabilidad del algoritmo.

Por otro lado, el archivo volumen_verlet_euler.py simula el movimiento de un oscilador armónico mediante el algoritmo de Verlet (simpléctico) y el de Euler (no simpléctico), mostrando cómo los algoritmos no simplécticos no conservan el volumen en el espacio de fases, luego no son estables, mientras que los simplécticos, sí.



# Trabajo de Fin de Grado — Dinámica Molecular  
**Joaquín Arcila Pérez**

Repositorio oficial del código asociado al Trabajo de Fin de Grado:

**"Revisión bibliográfica sobre Dinámica Molecular. Modelización, algoritmos y aplicaciones"**

Doble grado en Matemáticas e Ingeniería Informática – Universidad de Granada  
Autor: Joaquín Arcila Pérez
Tutor/es: Juan Calvo Yagüe, Lázaro René Izquierdo Fábregas
Curso académico: 2024–2025  

---

## 📄 Versiones del Documento

El Trabajo de Fin de Grado se encuentra disponible públicamente en las siguientes plataformas:

- 🎓 **Digibug (Repositorio institucional UGR)**:  
  https://hdl.handle.net/10481/108685

- 📊 **Figshare**:  
  https://doi.org/10.6084/m9.figshare.30786071

- 🌐 **Zenodo (con DOI)**:  
  https://doi.org/10.5281/zenodo.17817692

Estas versiones contienen la memoria completa del trabajo en formato PDF.

---

## 💻 Código Fuente

Este repositorio contiene los scripts implementados para apoyar la revisión bibliográfica realizada sobre la dinámica molecular.

En particular:

- **`sim_estabilidad_verlet.py`**  
  Simula el movimiento de un oscilador armónico mediante el algoritmo de **Verlet** para dos pasos de integración distintos, mostrando la influencia de dicho parámetro en la **estabilidad numérica** del algoritmo.

- **`volumen_verlet_euler.py`**  
  Simula el movimiento de un oscilador armónico mediante el algoritmo de **Verlet (simpléctico)** y el de **Euler (no simpléctico)**, mostrando cómo los algoritmos no simplécticos **no conservan el volumen en el espacio de fases** y, por tanto, no son estables, mientras que los simplécticos sí lo son.

---

## ⚙️ Requisitos

- Lenguaje principal: **Python 3**
- Librerías principales:
  - `numpy`
  - `matplotlib`
- Sistema operativo: Windows / Linux / macOS

---

## ▶️ Ejecución

Para ejecutar los scripts:

```bash
python sim_estabilidad_verlet.py
python volumen_verlet_euler.py

