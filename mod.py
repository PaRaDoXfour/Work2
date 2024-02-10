#mod.py

def sum_of_digits(n):
    # Конвертуємо число у строку, щоб можна було ітерувати по його цифрах
    digits_str = str(n)
    # Ініціалізуємо змінну для зберігання суми цифр
    total = 0
    # Ітеруємося по кожному символу у строковому представленні числа
    for digit_char in digits_str:
        # Перетворюємо символ у ціле число та додаємо його до суми
        total += int(digit_char)
    return total


# Функція для вводу числа користувачем та перевірки правильності вводу
def input_number(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Будь ласка, введіть правильне число.")
#mod.py

def sum_of_digits(n):
    # Конвертуємо число у строку, щоб можна було ітерувати по його цифрах
    digits_str = str(n)
    # Ініціалізуємо змінну для зберігання суми цифр
    total = 0
    # Ітеруємося по кожному символу у строковому представленні числа
    for digit_char in digits_str:
        # Перетворюємо символ у ціле число та додаємо його до суми
        total += int(digit_char)
    return total


# Функція для вводу числа користувачем та перевірки правильності вводу
def input_number(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Будь ласка, введіть правильне число.")
#mod.py

def sum_of_digits(n):
    # Конвертуємо число у строку, щоб можна було ітерувати по його цифрах
    digits_str = str(n)
    # Ініціалізуємо змінну для зберігання суми цифр
    total = 0
    # Ітеруємося по кожному символу у строковому представленні числа
    for digit_char in digits_str:
        # Перетворюємо символ у ціле число та додаємо його до суми
        total += int(digit_char)
    return total


# Функція для вводу числа користувачем та перевірки правильності вводу
def input_number(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Будь ласка, введіть правильне число.")
