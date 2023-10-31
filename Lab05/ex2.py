import pymc3 as pm

# Trace conține rezultatele inferenței Bayesiane
trace = trace  # Asigurați-vă că aveți trace-ul din modelul anterior

# Definim orele pentru cele 5 intervale
orele_intervale = [4, 7, 16, 19, 24]

# Definim o funcție pentru a obține capetele intervalelor și valorile λ
def gaseste_intervale_probabile(trace, orele_intervale):
    intervale_probabile = []
    valori_probabile = []
    
    for i in range(1, len(orele_intervale)):
        ora_inceput = orele_intervale[i - 1]
        ora_sfarsit = orele_intervale[i]
        
        # Filtrăm trace-ul pentru intervalul specific
        sub_trace = trace["λ"][(trace["λ"] > 0) & (trace["hour"] >= ora_inceput) & (trace["hour"] < ora_sfarsit)]
        
        # Afișăm percentila 2.5 și 97.5 pentru capetele intervalului
        interval_probabil = np.percentile(sub_trace, [2.5, 97.5])
        valoare_probabila = np.mean(sub_trace)
        
        intervale_probabile.append(interval_probabil)
        valori_probabile.append(valoare_probabila)
    
    return intervale_probabile, valori_probabile

intervale_probabile, valori_probabile = gaseste_intervale_probabile(trace, orele_intervale)

for i, interval in enumerate(intervale_probabile):
    print(f"Intervalul {i + 1}: Orele {orele_intervale[i]} - {orele_intervale[i + 1]}")
    print(f"Capete probabile: {interval[0]} - {interval[1]}")
    print(f"Valoare probabilă a parametrului λ: {valori_probabile[i]}\n")
