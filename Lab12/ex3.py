import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# Funcția pentru Metropolis
def metropolis(iterations, observed_data):
    # Valori inițiale și distribuție a priori (beta)
    alpha_prior = 2
    beta_prior = 2
    theta = np.random.beta(alpha_prior, beta_prior)  # Inițializare cu distribuția a priori
    
    # Stocare valori pentru theta
    samples = [theta]
    
    for _ in range(iterations):
        # Generare o propunere pentru o nouă valoare a lui theta folosind o distribuție normală
        theta_proposal = np.random.normal(theta, 0.1)
        
        # Calculul raportului de acceptare
        likelihood_current = np.prod(beta.pmf(observed_data, alpha_prior * theta, beta_prior * (1 - theta)))
        likelihood_proposal = np.prod(beta.pmf(observed_data, alpha_prior * theta_proposal, beta_prior * (1 - theta_proposal)))
        
        acceptance_ratio = min(1, likelihood_proposal / likelihood_current)
        
        # Alegerea unei valori noi pentru theta pe baza raportului de acceptare
        if np.random.uniform(0, 1) < acceptance_ratio:
            theta = theta_proposal
        
        samples.append(theta)
    
    return np.array(samples)

# Date observate (simulate pentru exemplu)
observed_data = np.random.binomial(n=1, p=0.7, size=100)

# Apelul funcției Metropolis
iterations = 10000
samples = metropolis(iterations, observed_data)

# Vizualizare rezultate
plt.hist(samples, bins=30, density=True, alpha=0.5, label='Metropolis (Beta prior)')
plt.title('Distribuția posterioară a lui theta folosind Metropolis și prior Beta')
plt.xlabel('Theta')
plt.ylabel('Densitatea probabilității')
plt.legend()
plt.show()
