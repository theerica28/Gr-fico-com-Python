import matplotlib.pyplot as plt
#Dados

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]

#Criar um gráfico de linha 
plt.bar(x, y)

#Adicionar rótulos aos eixos 
plt.xlabel('Eixo x')
plt.xlabel('Eixo y')

#Adicionnar um título ao gráfico

plt.title ('Exemplo de Gráfico de Linha')
#Mostrar o gráfico
plt.show()
