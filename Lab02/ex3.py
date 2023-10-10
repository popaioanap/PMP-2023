import random
import matplotlib.pyplot as plt

# Funcție pentru aruncarea unei monede cu probabilitatea specificată pentru stemă
def arunca_moneda(probabilitate_stema):
    return 's' if random.random() < probabilitate_stema else 'b'

# Funcție pentru simularea a 10 aruncări ale celor două monede
def simulare_aruncari(probabilitate_stema):
    rezultat = ''
    for _ in range(10):
        rezultat += arunca_moneda(probabilitate_stema)
    return rezultat

# Numărul de simulări
numar_simulari = 100

# Lista pentru a stoca rezultatele
rezultate = []

# Simulăm experimentul de 100 de ori și înregistrăm rezultatele
for _ in range(numar_simulari):
    rezultate.append(simulare_aruncari(0.3))

# Calculăm numărul de apariții pentru fiecare combinație posibilă
numar_ss = rezultate.count('ss')
numar_sb = rezultate.count('sb')
numar_bs = rezultate.count('bs')
numar_bb = rezultate.count('bb')

# Lista cu etichete pentru grafic
etichete = ['ss', 'sb', 'bs', 'bb']

# Lista cu numărul de apariții pentru fiecare combinație
numar_aparitii = [numar_ss, numar_sb, numar_bs, numar_bb]

# Creăm un grafic pentru distribuția rezultatelor
plt.bar(etichete, numar_aparitii)
plt.xlabel('Combinatii')
plt.ylabel('Numar de Aparitii')
plt.title('Distributia Rezultatelor in Experimentul cu Doua Monede')
plt.show()
