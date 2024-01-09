import numpy as np
import matplotlib.pyplot as plt

def estimate_pi(N):
    # Generează N puncte aleatoare în intervalul [0, 1] pentru x și y
    x = np.random.uniform(0, 1, N)
    y = np.random.uniform(0, 1, N)

    # Calculează distanța față de origine pentru fiecare punct
    distances = np.sqrt(x**2 + y**2)

    # Numără punctele care sunt în interiorul cercului
    points_inside_circle = np.sum(distances <= 1)

    # Calculează estimarea pentru π
    pi_estimate = 4 * (points_inside_circle / N)
    
    # Calculează eroarea estimării lui π
    error = np.abs(np.pi - pi_estimate)
    
    return error

# Numărul de puncte utilizate pentru estimare
Ns = [100, 1000, 10000]

# Rulăm estimarea de mai multe ori pentru fiecare N și stocăm erorile
errors = []
for N in Ns:
    # Numărul de rulări pentru fiecare N
    num_runs = 1000
    errors_N = [estimate_pi(N) for _ in range(num_runs)]
    errors.append(np.mean(errors_N))  # Calculăm media erorilor pentru fiecare N

# Calculăm deviația standard a erorilor pentru fiecare N
std_errors = [np.std(errors_N) for errors_N in errors]

# Vizualizăm rezultatele utilizând plt.errorbar()
plt.errorbar(Ns, errors, yerr=std_errors, fmt='o', capsize=5)
plt.xscale('log')  # Scalăm axa x pentru a vizualiza mai bine rezultatele pentru N-uri mari
plt.xlabel('Numărul de puncte (N)')
plt.ylabel('Eroare estimată pentru π')
plt.title('Eroarea estimată pentru π în funcție de numărul de puncte')
plt.grid(True)
plt.show()
