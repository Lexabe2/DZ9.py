import pandas as pd

# Задание
# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке
# sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)

dataframe = pd.read_csv('california_housing_test.csv')
resul = dataframe[dataframe['population'] < 501]['median_house_value'].agg(['mean'])
print(resul)

# Задача 42: Узнать какая максимальная households в зоне минимального значения population

dataframe = pd.read_csv('california_housing_test.csv')
resul = dataframe[dataframe['population'] == dataframe['population'].min()]['households'].max()
print(resul)