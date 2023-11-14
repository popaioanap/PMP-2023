# Definirea numărului de mostre și a lanțurilor pentru MCMC
num_samples = 1000
num_chains = 4

# Alegerea metodei de sampling
with linear_model:
    # Alegerea algoritmului de MCMC (e.g., Metropolis, NUTS)
    step = pm.NUTS()
    
    # Obținerea distribuțiilor posterioare folosind sampling MCMC
    trace = pm.sample(num_samples, step=step, chains=num_chains, random_seed=42)
    
# Exemplu de vizualizare a distribuțiilor posterioare ale coeficienților
pm.traceplot(trace, var_names=['intercept', 'slope_CP'])

# Calculul dreptei de regresie estimată pe baza distribuțiilor posterioare
intercept_mean = trace['intercept'].mean()
slope_CP_mean = trace['slope_CP'].mean()

# Trasarea dreptei de regresie
plt.figure(figsize=(8, 6))
plt.scatter(df['CP'], df['mpg'], alpha=0.7, label='Date observate')
plt.plot(df['CP'], intercept_mean + slope_CP_mean * df['CP'], color='red', label='Dreapta de regresie estimată')
plt.title('Regresie liniară între CP și mpg')
plt.xlabel('Cai putere (CP)')
plt.ylabel('Mile per Galon (mpg)')
plt.legend()
plt.grid(True)
plt.show()
