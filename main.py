import pyperclip
import time
import os

# Инициализация
file = open('Log.txt', 'w', encoding='utf-8')

# Добавление инфы в логи
def add(value):
    file.write(value + '\n')

# Мониторинг буфера обмена
def main():
    old = ''
    while True:
        new = pyperclip.paste()
        if new != old:
            add(new)
            old = new
        time.sleep(1)

if __name__ == "__main__":
    main()