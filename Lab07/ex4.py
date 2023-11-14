# Obținerea distribuției predictivă a posteriori
ppc = pm.sample_posterior_predictive(trace, samples=num_samples, model=linear_model)

# Calcularea intervalului HDI pentru distribuția predictivă a posteriori
mpg_pred = ppc['mpg']
hdi_95 = pm.hpd(mpg_pred, credible_interval=0.95)

# Trasarea graficului cu intervalul HDI
plt.figure(figsize=(8, 6))
plt.scatter(df['CP'], df['mpg'], alpha=0.7, label='Date observate')
plt.plot(df['CP'], intercept_mean + slope_CP_mean * df['CP'], color='red', label='Dreapta de regresie estimată')
plt.fill_between(df['CP'], hdi_95[:, 0], hdi_95[:, 1], color='orange', alpha=0.3, label='Intervalul HDI 95%')
plt.title('Regresie liniară între CP și mpg')
plt.xlabel('Cai putere (CP)')
plt.ylabel('Mile per Galon (mpg)')
plt.legend()
plt.grid(True)
plt.show()
