## ОП Python / 12. Основы работы с PyQT6 (создание приложений под Desktop) (доп-но)

### Введение

**PyQt6** - это библиотека для создания графических пользовательских интерфейсов (**GUI**) на языке Python. Она позволяет разработчикам создавать приложения с графическим интерфейсом для рабочих столов (_desktop applications_) на различных операционных системах, включая **Windows**, **macOS** и **Linux**. 
Вот основы работы с **PyQt6** для создания Desktop-приложений:

Установите библиотеку PyQt6 с помощью pip: 

    pip install PyQt6


### Создание Окна GUI

Создайте базовое окно приложения. В **PyQt6** это делается с использованием класса **QApplication** и **QMainWindow**. 
Пример:

```python
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Мое PyQt6 Приложение")
window.setGeometry(100, 100, 800, 600)  # Установка размеров окна

window.show()
sys.exit(app.exec())
```

В этом примере создается окно приложения с заголовком и размерами.

### Добавление виджетов (кнопка)

```python
from PyQt6.QtWidgets import QPushButton

button = QPushButton("Нажми меня", window)
button.setGeometry(50, 50, 200, 30)  # Установка размеров кнопки и ее положения
```

создание и обработка события нажатия на кнопку

```python
def button_click():
    print("Кнопка была нажата!")
button.clicked.connect(button_click)
```

Запустите ваше приложение с помощью **app.exec()**. Весь код для создания и настройки окон и виджетов должен быть размещен перед этой строкой.

```python
sys.exit(app.exec())
```

[PyQt6](https://pypi.org/project/PyQt6/)
