from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination


# Crearea unui obiect pentru rețeaua Bayesiană
model = BayesianNetwork([('E', 'F'), ('F', 'A')])

# Definirea probabilităților marginale
cpd_e = TabularCPD(variable='E', variable_card=2, values=[[0.9995], [0.0005]])
cpd_f = TabularCPD(variable='F', variable_card=2, values=[[0.99], [0.01]])

# Definirea probabilităților condiționate
cpd_a = TabularCPD(variable='A', variable_card=2, values=[[0.9999, 0.03, 0.9998, 0.02],
                                                        [0.0001, 0.97, 0.0002, 0.98]],
                  evidence=['E', 'F'], evidence_card=[2, 2])

# Adăugarea probabilităților la model
model.add_cpds(cpd_e, cpd_f, cpd_a)

# Verificarea consistenței modelului
assert model.check_model()

# Crearea unui obiect pentru inferență
inference = VariableElimination(model)

# Exemplu de inferență: probabilitatea ca alarma să se declanșeze
result = inference.query(variables=['A'])
print(result)
