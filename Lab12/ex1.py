import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# Distribuție a priori originală (uniformă)
alpha_prior = 1
beta_prior = 1

# Distribuție a priori alternativă
grid = np.linspace(0, 1, 1000)
prior_alt_1 = (grid <= 0.5).astype(int)
prior_alt_2 = np.abs(grid - 0.5)

# Generarea unui set de date observate
# Vom simula generarea a 500 de date binare (0 sau 1)
np.random.seed(42)
observed_data = np.random.binomial(n=1, p=0.7, size=500)

# Calculul parametrilor a posteriori folosind distribuția a priori originală
alpha_posterior = alpha_prior + np.sum(observed_data)
beta_posterior = beta_prior + len(observed_data) - np.sum(observed_data)

# Calculul parametrilor a posteriori folosind distribuția a priori alternativă
alpha_posterior_alt_1 = np.sum(prior_alt_1 * observed_data) + alpha_prior
beta_posterior_alt_1 = np.sum(prior_alt_1 * (1 - observed_data)) + beta_prior

alpha_posterior_alt_2 = np.sum(prior_alt_2 * observed_data) + alpha_prior
beta_posterior_alt_2 = np.sum(prior_alt_2 * (1 - observed_data)) + beta_prior

# Calculul distribuției a posteriori
posterior = beta(alpha_posterior, beta_posterior).pdf(grid)
posterior_alt_1 = beta(alpha_posterior_alt_1, beta_posterior_alt_1).pdf(grid)
posterior_alt_2 = beta(alpha_posterior_alt_2, beta_posterior_alt_2).pdf(grid)

# Vizualizarea rezultatelor
plt.figure(figsize=(10, 6))

plt.plot(grid, posterior, label='Posterior (Prior Uniform)')
plt.plot(grid, posterior_alt_1, label='Posterior (Prior Alt 1)')
plt.plot(grid, posterior_alt_2, label='Posterior (Prior Alt 2)')

plt.title('Inferență Bayesiană cu diferite distribuții a priori')
plt.xlabel('Valoarea parametrului')
plt.ylabel('Densitatea probabilității')
plt.legend()
plt.show()
