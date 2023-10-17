from pgmpy.inference import VariableElimination

# Crearea un obiect pentru inferență pe modelul existent
inference = VariableElimination(model)

# Calcularea probabilității că a avut loc un incendiu, fără ca alarma de incendiu să se activeze
# Acest lucru corespunde probabilității P(F="a avut loc incendiu" | A="alarmă nu a fost declanșată")
result = inference.query(variables=['F'], evidence={'A': 0})
print(result)
