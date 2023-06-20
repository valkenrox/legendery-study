import pandas as pd
import seaborn as srn
import statistics as sts
import matplotlib.pyplot as plt



base_csv = pd.read_csv('C:\\Users\\soloq\\Desktop\\Curso Python\\Anotações Aula\\inicio\\exercicios\\Churn.csv', sep=';')
# base_csv = pd.read_csv('C:\Users\soloq\Desktop\Curso Python\Anotações Aula\inicio\exercicios\Churn.csv', sep=';')


# print(base_csv.head()) BASE SEM NOME NAS COLUNAS
# print(base_csv.shape)
base_csv.columns = ['Id', 'Score', 'Estado', 'Genero', 'Idade', 'Patrimonio', 'Saldo', 'Produtos', 'TemCartCredito', 'Ativo', 'Salario', 'Saiu'] # NOMEANDO AS COLUNAS
print(base_csv.head())

agrupado = base_csv.groupby(['Estado']).size()

print(agrupado)

plt.bar(agrupado.index, agrupado.values)

plt.title('Clientes por Estado')
plt.xlabel('Estados')
plt.show()

# print(plt.bar(agrupado.index, agrupado.values))