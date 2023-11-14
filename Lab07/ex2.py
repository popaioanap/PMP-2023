import pymc3 as pm
import pandas as pd

# Încarcarea setului de date într-un DataFrame
df = pd.read_csv('auto-mpg.csv')

# Definirea modelului în PyMC
with pm.Model() as linear_model:
    # Coeficienții pentru intercept și pentru variabila independentă
    intercept = pm.Normal('intercept', mu=0, sd=10)
    slope_CP = pm.Normal('slope_CP', mu=0, sd=10)
    
    # Variabila dependentă estimată
    mu = intercept + slope_CP * df['CP']
    
    # Variabilitatea datelor
    sigma = pm.HalfNormal('sigma', sd=10)
    
    # Definirea distribuției normale pentru variabila dependentă
    mpg = pm.Normal('mpg', mu=mu, sd=sigma, observed=df['mpg'])
