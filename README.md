## ОП Python / 9.Автоматизация процессов

### 9.1 Автоматизация работы с файлами и папками

Эта задача заключается в том, чтобы использовать **Python** для выполнения различных действий с _файлами_ и _папками_ на компьютере. Например, создание новой папки, копирование файлов, переименование и удаление файлов и папок. 

Давайте рассмотрим простые примеры:

_Пример 1_ Создание новой папки и файла

```python
import os

# Создание новой папки
os.mkdir("Новая_папка")

# Переход в эту папку
os.chdir("Новая_папка")

# Создание нового текстового файла и запись в него данных
with open("новый_файл.txt", "w") as file:
    file.write("Привет, мир!")
```


_Пример 2_ Переименование файла и папки

```python
import os

# Переименование файла
os.rename("старое_имя.txt", "новое_имя.txt")

# Переименование папки
os.rename("старое_название_папки", "новое_название_папки")
```

_Пример 3_ Удаление файла и папки

```python
import os

# Удаление файла
os.remove("файл_для_удаления.txt")

# Удаление папки (папка должна быть пустой)
os.rmdir("папка_для_удаления")
```

### 9.2 Автоматизация интернет-действий с Selenium
**Selenium** - это инструмент для автоматизации действий веб-браузера, таких как запуск браузера, навигация по веб-сайтам, заполнение форм, клики и извлечение данных. 

_Пример_ автоматизации поиска в Google:

```python
import time
from selenium import webdriver

# Запуск браузера (пример для Chrome)
driver = webdriver.Chrome()

# Открытие сайта Google
driver.get("https://www.google.com")

time.sleep(1)
# Нахождение поля для ввода текста и ввод текста
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python")

time.sleep(1)
# Нажатие кнопки "Поиск"
search_button = driver.find_element(By.NAME, "btnK")
search_button.click()

```

### 9.3 Автоматизация работы с каким-то сайтом (сервисом)

Это связано с использованием библиотек и инструментов для автоматизации работы с конкретным веб-сайтом или веб-сервисом. 

_Например_, автоматическое вход в аккаунт на сайте и извлечение информации:

```python
import requests
from bs4 import BeautifulSoup

# Создание сессии для авторизации на сайте
session = requests.Session()
login_url = "https://example.com/login"
payload = {"username": "your_login", "password": "your_password"}
session.post(login_url, data=payload)

# Запрос страницы после авторизации
profile_url = "https://example.com/profile"
response = session.get(profile_url)

# Извлечение информации с помощью BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")
user_info = soup.find("div", class_="user-info")
print(user_info.text)
```
В данном случае, мы автоматизировали вход на сайт и извлекли информацию о пользователе с использованием библиотеки requests для HTTP-запросов и BeautifulSoup для парсинга HTML-кода.

[ПОДРОБНЕЕ О SELENIUM](https://pypi.org/project/selenium/)
