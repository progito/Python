## ОП Python / 10.Excel работа с данными используя Python

### Введение

**Зачем работать с данными Excel в Python?**

**Данные Excel** - один из наиболее распространенных форматов хранения и обмена данными в офисной среде.

Многие компании и организации используют **Excel** для записи и хранения данных, таких как финансовые отчеты, инвентаризация, базы данных клиентов и многое др.

_Работа с данными Excel_ позволяет **эффективно** анализировать, визуализировать и обрабатывать большие объемы информации.

\
**Преимущества использования Python и Pandas для обработки данных Excel:**

**Python** - мощный и гибкий ЯП, который позволяет автоматизировать множество задач, связанных с данными **Excel**.

**Pandas** - библиотека для Python, специализирующаяся на работе с данными, предоставляет множество удобных инструментов для чтения, обработки и анализа данных **Excel**.

**Python и Pandas** позволяют создавать **собственные сценарии** обработки данных, что особенно полезно, когда нужно регулярно обновлять, фильтровать или анализировать данные в **Excel**.

\
**Типичные сценарии использования:**

**Анализ данных** - **Python** и **Pandas** позволяют проводить сложный анализ данных **Excel**, выявлять тренды, строить графики и вычислять статистики.

**Автоматизация задач** - вы можете создать скрипты **Python** для автоматизации рутиных задач, таких как обновление данных, конвертация форматов или фильтрация информации.

**Создание отчетов**- **Python** может исп-ся для создания кастомных отчетов на основе данных **Excel**, которые соответствуют вашим потребностям.

**Создание дашбордов** - вы можете исп-ть **Python** для создания интерактивных **дашбордов** и визуализаций данных на основе данных **Excel**.

### Установка Pandas

_CMD:_ 

    pip install pandas

### Google Sheets Python

Установка _CMD:_ 

    pip install gspread

Работа с **Google Sheets** в **Python** может быть выполнена с исп-м библиотеки _gspread_. Эта библиотека позволяет взаимодействовать с таблицами **Google Sheets**, читать и записывать данные, создавать новые таблицы и многое др.

Пример чтения данных из Google Sheets:

```python
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Указываем путь к файлу с учетными данными (Service Account Key)
credentials = ServiceAccountCredentials.from_json_keyfile_name('your-credentials.json', ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'])

# Авторизация
gc = gspread.authorize(credentials)

# Открываем таблицу по URL или по имени
worksheet = gc.open('Название таблицы').sheet1

# Чтение данных
data = worksheet.get_all_records()
print(data)
```

Запись данных

```python
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Указываем путь к файлу с учетными данными (Service Account Key)
credentials = ServiceAccountCredentials.from_json_keyfile_name('your-credentials.json', ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'])

# Авторизация
gc = gspread.authorize(credentials)

# Открываем таблицу по URL или по имени
worksheet = gc.open('Название таблицы').sheet1

# Чтение данных
data = worksheet.get_all_records()
print(data)
```
[PANDAS documentation](https://pandas.pydata.org/docs/)
[GSPREAD documentation](https://docs.gspread.org/en/v5.10.0/)
