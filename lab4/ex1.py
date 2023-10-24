import numpy as np
from scipy.stats import poisson, norm, expon

lambda_clienti = 20
media_plasare_plata = 2  # minute
deviatie_standard_plasare_plata = 0.5  # minute
media_gatit = 3  # minute (α)

numar_clienti = poisson.rvs(lambda_clienti)

timp_plasare_plata = norm.rvs(loc=media_plasare_plata, scale=deviatie_standard_plasare_plata)

timp_gatit = expon.rvs(scale=media_gatit)

timp_total = timp_plasare_plata + timp_gatit

print("Număr de clienți într-o oră:", numar_clienti)
print("Timp de plasare și plată pentru o comandă (minute):", timp_plasare_plata)
print("Timp de gătit pentru o comandă (minute):", timp_gatit)
print("Timp total pentru o comandă (minute):", timp_total)
