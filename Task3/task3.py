import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Товар': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A'],
    'Цена': [100, 150, np.nan, 120, 160, 200, 110, np.nan, 190, 130],
    'Количество': [10, 5, 15, 1200, 8, 12, 9, 6, 1500, 11]
}

df = pd.DataFrame(data)

# заполняю пропуски медианой
df['Цена'] = df['Цена'].fillna(df['Цена'].median())

# удаляю выбросы
df = df[(df['Количество'] >= 1) & (df['Количество'] <= 1000)]

# общая стоимость
df['Общая_стоимость'] = df['Цена'] * df['Количество']

# группировка по товарам
revenue = df.groupby('Товар')['Общая_стоимость'].sum()

# график
revenue.plot(kind='bar')
plt.show()