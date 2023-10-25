from scipy.stats import expon

probabilitate_gatit_sub_15_min = expon.cdf(15, scale=alpha)

probabilitate_total_sub_15_min = probabilitate_gatit_sub_15_min**4

import numpy as np

alpha_max = 0
probabilitate_total_sub_15_min = 0
while probabilitate_total_sub_15_min < 0.95:
    alpha_max += 0.01  # Incrementăm α pentru a găsi valoarea maximă
    probabilitate_gatit_sub_15_min = expon.cdf(15, scale=alpha_max)
    probabilitate_total_sub_15_min = probabilitate_gatit_sub_15_min**4

print("Valoarea maximă a lui alpha pentru o probabilitate de 95% este:", alpha_max)

