import pymc3 as pm
import arviz as az

# Date observate pentru Y
observed_data = [0, 5, 10]

# Definirea modelelor pentru diferite combinații de Y și θ
with pm.Model() as model:
    for Y in observed_data:
        for theta in [0.2, 0.5]:
            n = pm.Poisson("n", mu=10)
            Y_obs = pm.Binomial("Y_obs", n=n, p=theta, observed=Y)

# Am folosit Observations pentru a înregistra datele observate pentru Y

# MCMC (lanț Markov în cadrul Monte Carlo) pentru a obține distribuția a posteriori
with model:
    trace = pm.sample(5000, tune=1000, chains=4)

# Vizualizarea rezultatelor cu arviz
az.plot_posterior(trace, var_names=["n"])
