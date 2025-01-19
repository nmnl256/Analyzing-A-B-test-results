import pandas as pd
import matplotlib.pyplot as plt
file_path = 'ab_test.csv'

# Укажем движок 'openpyxl' для чтения Excel файла
data = pd.read_csv(file_path, sep=";")
# Пример анализа
control_group = data[data["group"] == 'Control']
test_group = data[data["group"] == 'Test']

# Вычисляем среднее значение метрики для каждой группы
mean_control = control_group['success'].mean()
mean_test = test_group['success'].mean()
# Печатаем результаты
print(f"Средняя метрика для контрольной группы: {mean_control:.4f}")
print(f"Средняя метрика для тестовой группы: {mean_test:.4f}")


# Разделим данные по дням
data['week'] = pd.to_datetime(data['date'], format="%d.%m.%Y").dt.isocalendar().week

# Показатели по неделям
weekly_data = data.groupby(['week', 'group'])['success'].mean().unstack()
weekly_data.plot(kind='line', figsize=(10, 6))
plt.title("Конверсия по неделям")
plt.xlabel("Неделя")
plt.ylabel("Конверсия")
plt.show()