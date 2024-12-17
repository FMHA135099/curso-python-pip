import csv
#Solo sera lectura se usara 'r'
def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter= ',')
    #Se le asigna a header y se une al row y generarlo como diccionario
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data  

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])