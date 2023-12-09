import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

gorjeta = sns.load_dataset('tips')
print(gorjeta.head())

'''
# Histograma
sns.histplot(gorjeta['total_bill'], kde=True, bins=30)

# Plotagem comparada
sns.jointplot(x = 'total_bill', y = 'tip', data= gorjeta)

sns.jointplot(x = 'total_bill', y = 'tip', data= gorjeta, kind='hex')


sns.jointplot(x = 'total_bill', y = 'tip', data= gorjeta, kind='reg')

Todas as variáveis
sns.pairplot(gorjeta, hue='sex')
sns.countplot(x='sex', data=gorjeta)


#Diagrama de caixas

sns.boxplot(x = 'day', y = 'total_bill', data= gorjeta)
plt.show()
sns.boxplot(x = 'day', y = 'total_bill', data= gorjeta, hue='smoker')
plt.show()


# Diagrama de violino
sns.violinplot(x = 'day', y = 'total_bill', data=gorjeta)
plt.show()
sns.violinplot(x = 'day', y = 'total_bill', data=gorjeta, hue='smoker', split=True) #O valor split sendo verdadeiro permite analisar o valor de 'sex' no mesmo violino

#Grafico de enxame
sns.swarmplot(x = 'day', y = 'total_bill', data=gorjeta, hue='smoker')
'''
#coringa
sns.catplot(x = 'day', y = 'total_bill', kind='bar', data=gorjeta, hue='smoker')
plt.show()