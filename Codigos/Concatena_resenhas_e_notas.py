import pandas as pd

datahead_notas = pd.read_csv('Notas/Notas1.csv').iloc[:, 1:]
datahead_resenhas = pd.read_csv('Resenhas/Resenhas1.csv').iloc[:, 1:]

for a in range(2, 10, 1):
    dataset_notas = pd.read_csv('Notas/Notas' + str(a) + '.csv').iloc[:, 1:]
    dataset_resenhas = pd.read_csv('Resenhas/Resenhas' + str(a) + '.csv').iloc[:, 1:]
    datahead_notas = pd.concat([datahead_notas, dataset_notas], ignore_index=True)
    datahead_resenhas = pd.concat([datahead_resenhas, dataset_resenhas], ignore_index=True)

datahead_notas.to_csv('Notas.csv')
datahead_resenhas.to_csv('Resenhas.csv')
