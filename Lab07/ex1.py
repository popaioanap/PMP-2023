import pandas as pd
import matplotlib.pyplot as plt

# Încarcarea setului de date într-un DataFrame
df = pd.read_csv('auto-mpg.csv')

# Vizualizarea iniţială a datelor
print(df.head())

# Curăţarea datelor (dacă este necesar)
# Verificarea datelor lipsă sau atipice și eliminarea lor

# Trasarea graficului pentru relaţia dintre CP şi mpg
plt.figure(figsize=(8, 6))
plt.scatter(df['CP'], df['mpg'], alpha=0.7)
plt.title('Relaţia dintre CP şi mpg')
plt.xlabel('Cai putere (CP)')
plt.ylabel('Mile per Galon (mpg)')
plt.grid(True)
plt.show()
