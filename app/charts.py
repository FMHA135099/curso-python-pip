#Crear graficas con matplotlib
import matplotlib.pyplot as plt
#Grafica de barras
def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./imgs/{name}.png')
  plt.close()
#Grafica de pastel
def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig('pie.png')
  plt.close()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 40, 800]
  #Se cambia pie o bar dependiendo la grafica que se quiera
  generate_pie_chart(labels, values)
  