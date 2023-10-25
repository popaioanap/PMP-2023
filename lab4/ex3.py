lambda_parameter = 20  # rata de sosire a clienților în clienți/oră
mu = 1 / alpha  # rata de servire în clienți/oră (din calculele anterioare)

Wq = lambda_parameter / (mu * (mu - lambda_parameter))

print("Timpul mediu de așteptare al unui client este:", Wq, "minute")
