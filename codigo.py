import pandas as pd
import matplotlib.pyplot as plt
import os

dados = pd.read_csv('teste1.csv')

plt.figure(figsize=(10, 6))
plt.bar(dados['Country'], dados['Population'], color='skyblue')
plt.xlabel('País')
plt.ylabel('População')
plt.title('População de cada país')
plt.xticks(rotation=45)
plt.tight_layout()

if not os.path.exists('app_teste/templates/images'):
    os.makedirs('app_teste/templates/images')
plt.savefig('app_teste/templates/images/grafico.png')
