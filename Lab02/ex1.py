import numpy as np
import matplotlib.pyplot as plt

# Parametrii distributiei exponențiale pentru cei doi mecanici
lambda1 = 4  # Pentru primul mecanic
lambda2 = 6  # Pentru al doilea mecanic

# Probabilitatea ca un client să fie servit de primul mecanic
p_primul_mecanic = 0.4

# Numărul de valori pe care dorim să le generăm
numar_valori = 10000

# Generăm valorile pentru timpul de servire X pentru fiecare client
timp_servire = []
for _ in range(numar_valori):
    # Decide dacă clientul va fi servit de primul mecanic sau de al doilea
    if np.random.rand() < p_primul_mecanic:
        timp_servire.append(np.random.exponential(1 / lambda1))
    else:
        timp_servire.append(np.random.exponential(1 / lambda2))

# Calculăm media și deviația standard a timpului de servire
media = np.mean(timp_servire)
deviatia_standard = np.std(timp_servire)

print("Media timpului de servire (X):", media)
print("Deviația standard a timpului de servire (X):", deviatia_standard)

# Realizăm un grafic al densității distribuției lui X
plt.hist(timp_servire, bins=50, density=True, alpha=0.6, color='g')
plt.xlabel("Timp de servire (X)")
plt.ylabel("Densitate")
plt.title("Densitatea distribuției lui X")
plt.show()