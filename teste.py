import numpy as np
import matplotlib.pyplot as plt
p = []
t = np.arange(0, 52)
for i in t:
    p.append(np.log(1-np.random.gamma(1.88, 0.008))/np.log(0.999306))
    soma = 0
for i in p:
    soma = soma + i
print(p)