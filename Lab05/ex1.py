import pymc3 as pm
import numpy as np

# Datele observate (valorile traficului înregistrate în fiecare minut)
data = np.array([valori_trafic])

# Definim o distribuție prior pentru parametrul λ
λ = pm.Exponential("λ", lam=1.0)

# Definim ratele pentru fiecare interval orar
# Ratele se schimbă în jurul orelor specificate
rate = pm.math.switch(
    pm.math.eq(ora, [7, 16, 8, 19]),
    λ * 1.2,  # Creștere cu 20%
    λ
)

# Definim distribuția Poisson pentru datele observate
trafic = pm.Poisson("trafic", mu=rate, observed=data)

# Creăm un model PyMC
model = pm.Model()

# Realizăm inferența Bayesiană
with model:
    trace = pm.sample(2000, tune=1000)

# Afișăm rezultatele inferenței
pm.summary(trace)
pm.traceplot(trace)
