import math
import random
from mesa import Model, Agent
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector

def mm1k_metrics(tasa_llegada, tasa_servicio, capacidad):
    rho = tasa_llegada / tasa_servicio if tasa_servicio > 0 else float('inf')
    if abs(rho - 1.0) > 1e-12:
        p0 = (1 - rho) / (1 - rho**(capacidad+1))
    else:
        p0 = 1.0 / (capacidad+1)
    p = [p0 * (rho**n) for n in range(capacidad+1)]
    if abs(rho - 1.0) > 1e-12:
        L = (rho * (1 - (capacidad+1)*rho**capacidad + capacidad*rho**(capacidad+1))) / ((1 - rho)*(1 - rho**(capacidad+1)))
    else:
        L = capacidad / 2.0
    pK = p[-1]
    tasa_efectiva = tasa_llegada * (1 - pK)
    prob_ocupado = 1 - p0
    Lq = L - prob_ocupado
    if tasa_efectiva > 0:
        W = L / tasa_efectiva
        Wq = Lq / tasa_efectiva
    else:
        W = float('inf')
        Wq = float('inf')
    return {
        'rho': rho, 'p0': p0, 'pK': pK,
        'L': L, 'Lq': Lq,
        'lambda_eff': tasa_efectiva,
        'W': W, 'Wq': Wq,
        'p': p
    }

class Usuario(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.tiempo_llegada = None
        self.tiempo_inicio_servicio = None
        self.tiempo_fin_servicio = None

class Cajero(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.ocupado = False

class ModeloCola(Model):
    def __init__(self, tasa_llegada, tasa_servicio, capacidad, tiempo_max):
        self.tasa_llegada = tasa_llegada
        self.tasa_servicio = tasa_servicio
        self.capacidad = capacidad
        self.tiempo_max = tiempo_max
        self.schedule = RandomActivation(self)
        self.cola = []
        self.cajero = Cajero("cajero", self)
        self.schedule.add(self.cajero)
        self.next_id = 0
        self.datacollector = DataCollector(
            model_reporters={
                "Usuarios_en_sistema": lambda m: len(m.cola) + (1 if m.cajero.ocupado else 0),
                "Usuarios_en_cola": lambda m: len(m.cola)
            }
        )

    def step(self):
        if random.random() < self.tasa_llegada * 1.0:
            if len(self.cola) + (1 if self.cajero.ocupado else 0) < self.capacidad:
                usuario = Usuario(self.next_id, self)
                self.next_id += 1
                usuario.tiempo_llegada = self.schedule.time
                self.cola.append(usuario)
        if (not self.cajero.ocupado) and (len(self.cola) > 0):
            u = self.cola.pop(0)
            self.cajero.ocupado = True
            u.tiempo_inicio_servicio = self.schedule.time
            servicio = random.expovariate(self.tasa_servicio)
            u.tiempo_fin_servicio = u.tiempo_inicio_servicio + servicio
        self.datacollector.collect(self)
        self.schedule.step()

    def run_model(self):
        for t in range(self.tiempo_max):
            self.step()

def simular_varios_escenarios(lista_parametros, tiempo_max=10000):
    resultados = []
    for (tasa_llegada, tasa_servicio, capacidad) in lista_parametros:
        modelo = ModeloCola(tasa_llegada, tasa_servicio, capacidad, tiempo_max)
        modelo.run_model()
        df = modelo.datacollector.get_model_vars_dataframe()
        prom_sistema = df["Usuarios_en_sistema"].mean()
        prom_cola = df["Usuarios_en_cola"].mean()
        teorico = mm1k_metrics(tasa_llegada, tasa_servicio, capacidad)
        resultados.append({
            'lambda': tasa_llegada,
            'mu': tasa_servicio,
            'K': capacidad,
            'obs_sistema': prom_sistema,
            'obs_cola': prom_cola,
            'teo_L': teorico['L'],
            'teo_Lq': teorico['Lq'],
            'teo_W': teorico['W'],
            'teo_Wq': teorico['Wq'],
            'rho': teorico['rho']
        })
    return resultados

if __name__ == "__main__":
    escenarios = [
        (0.4, 1.0, 4),
        (0.8, 1.0, 6),
        (1.1, 1.5, 5),
        (1.5, 2.0, 7)
    ]
    resultados = simular_varios_escenarios(escenarios, tiempo_max=15000)
    for r in resultados:
        print(f"Escenario λ={r['lambda']}, μ={r['mu']}, K={r['K']}")
        print(f" → Observado: Ns={r['obs_sistema']:.3f}, Nw={r['obs_cola']:.3f}")
        print(f" → Teórico: L={r['teo_L']:.3f}, Lq={r['teo_Lq']:.3f}, W={r['teo_W']:.3f}, Wq={r['teo_Wq']:.3f}, ρ={r['rho']:.3f}")
        print("---------------------------------------------------")
