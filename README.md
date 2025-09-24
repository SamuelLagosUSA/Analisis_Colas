# Análisis de Cola M/M/1

Este documento presenta la comparación entre los valores **teóricos** y los resultados obtenidos por **simulación en NetLogo** para una cola M/M/1 con distintos valores de tasa de llegada $\lambda$ y tiempo medio de servicio.

---

# Prueba 1: $\lambda = 0.4$

### Cálculos teóricos

1. $\mu = \tfrac{1}{1.2} = 0.8333$  
2. $\rho = \tfrac{0.4}{0.8333} = 0.48$  
3. $N_s = \tfrac{0.48}{1-0.48} = 0.923$  
4. $T_s = \tfrac{1}{0.8333 - 0.4} = 2.308$  
5. $N_w = \tfrac{0.48^2}{1-0.48} = 0.443$  
6. $T_w = \tfrac{0.48}{0.8333 - 0.4} = 1.108$  

### Resultados de la simulación

<img width="819" height="408" alt="image" src="https://github.com/user-attachments/assets/6dcd486b-3fd7-4a0c-ab5c-7e64f47cb216" />

| Métrica | Teórico | Simulación | Diferencia (Δ) | Error relativo (%) |
|--------:|--------:|-----------:|---------------:|-------------------:|
| Ns      | 0.923   | 0.922      | -0.001         | 0.11 %             |
| Ts      | 2.308   | 2.305      | -0.003         | 0.13 %             |
| Nw      | 0.443   | 0.442      | -0.001         | 0.23 %             |
| Tw      | 1.108   | 1.106      | -0.002         | 0.18 %             |

---

# Prueba 2: $\lambda = 0.2$

### Cálculos teóricos

1. $\mu = \tfrac{1}{1.2} = 0.8333$  
2. $\rho = \tfrac{0.2}{0.8333} = 0.24$  
3. $N_s = \tfrac{0.24}{1-0.24} = 0.316$  
4. $T_s = \tfrac{1}{0.8333 - 0.2} = 1.600$  
5. $N_w = \tfrac{0.24^2}{1-0.24} = 0.076$  
6. $T_w = \tfrac{0.24}{0.8333 - 0.2} = 0.384$  

### Resultados de la simulación

<img width="847" height="412" alt="image" src="https://github.com/user-attachments/assets/b9cadfe0-d814-4d52-a35d-f155dd0a5a18" />

| Métrica | Teórico | Simulación | Diferencia (Δ) | Error relativo (%) |
|--------:|--------:|-----------:|---------------:|-------------------:|
| Ns      | 0.316   | 0.315      | -0.001         | 0.32 %             |
| Ts      | 1.600   | 1.597      | -0.003         | 0.19 %             |
| Nw      | 0.076   | 0.076      |  0.000         | 0.00 %             |
| Tw      | 0.384   | 0.383      | -0.001         | 0.26 %             |

---

# Prueba 3: $\lambda = 0.3$

### Cálculos teóricos

1. $\mu = \tfrac{1}{1.2} = 0.8333$  
2. $\rho = \tfrac{0.3}{0.8333} = 0.36$  
3. $N_s = \tfrac{0.36}{1-0.36} = 0.5625$  
4. $T_s = \tfrac{1}{0.8333 - 0.3} = 1.875$  
5. $N_w = \tfrac{0.36^2}{1-0.36} = 0.2025$  
6. $T_w = \tfrac{0.36}{0.8333 - 0.3} = 0.675$  

### Resultados de la simulación

<img width="847" height="421" alt="image" src="https://github.com/user-attachments/assets/f28dfa5f-7fe2-4ace-9724-95d663e7ee34" />

| Métrica | Teórico | Simulación | Diferencia (Δ) | Error relativo (%) |
|--------:|--------:|-----------:|---------------:|-------------------:|
| Ns      | 0.563   | 0.560      | -0.003         | 0.44 %             |
| Ts      | 1.875   | 1.865      | -0.010         | 0.53 %             |
| Nw      | 0.203   | 0.202      | -0.001         | 0.25 %             |
| Tw      | 0.675   | 0.670      | -0.005         | 0.74 %             |

---

# Conclusión

En las tres pruebas realizadas, los resultados simulados se aproximan de forma **muy precisa** a los valores teóricos.  
Los errores relativos en todas las métricas se mantienen **menores al 1%**, validando la consistencia del modelo de simulación respecto a la teoría de colas M/M/1.

