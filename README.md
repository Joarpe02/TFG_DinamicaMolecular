# Bachelor’s Thesis — Molecular Dynamics  
**Joaquín Arcila Pérez**

Official code repository associated with the Bachelor’s Thesis:

**"Bibliographic Review on Molecular Dynamics. Modelling, Algorithms and Applications"**

Double Degree in Mathematics and Computer Engineering – University of Granada<br>
Author: Joaquín Arcila Pérez<br>
Supervisors: Juan Calvo Yagüe, Lázaro René Izquierdo Fábregas<br>
Academic year: 2024–2025  

---

## 📄 Thesis Document Versions

The Bachelor’s Thesis is publicly available on the following platforms:

- 🎓 **Digibug (Institutional Repository of the University of Granada)**  
  https://hdl.handle.net/10481/108685

- 📊 **Figshare**  
  https://doi.org/10.6084/m9.figshare.30786071

- 🌐 **Zenodo (with DOI)**  
  https://doi.org/10.5281/zenodo.17817692

These links provide access to the full PDF version of the thesis.

---

## 💻 Source Code

This repository contains the scripts implemented to support the bibliographic review on Molecular Dynamics.

In particular:

- **`sim_estabilidad_verlet.py`**  
  Simulates the motion of a harmonic oscillator using the **Verlet algorithm** for two different integration time steps, showing the influence of this parameter on the **numerical stability** of the algorithm.

- **`volumen_verlet_euler.py`**  
  Simulates the motion of a harmonic oscillator using both the **Verlet algorithm (symplectic)** and the **Euler algorithm (non-symplectic)**, showing how non-symplectic algorithms **do not preserve volume in phase space** and are therefore unstable, whereas symplectic algorithms do preserve it.

---

## ⚙️ Requirements

- Main language: **Python 3**
- Main libraries:
  - `numpy`
  - `matplotlib`
- Operating system: Windows / Linux / macOS

---

## ▶️ Execution

To run the scripts:

```bash
python sim_estabilidad_verlet.py
python volumen_verlet_euler.py
