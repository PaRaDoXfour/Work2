import math


def calculate_z(x):
    z = math.exp(x) + math.sqrt(x)
    return z


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


# Головна функція програми
def main():
    # Вводимо число x
    x = input_number("Введіть значення x: ")
    # Обчислюємо z
    z = calculate_z(x)
    # Виводимо результат
    print(f"Результат обчислення z: {z}")

    # Вводимо число n
    n = input_number("Введіть число n: ")
    # Знаходимо суму його цифр
    digit_sum = sum_of_digits(n)
    # Виводимо результат
    print(f"Сума цифр числа {n}: {digit_sum}")


# Викликаємо головну функцію програми
if __name__ == "__main__":
    main()
import math


def calculate_z(x):
    z = math.exp(x) + math.sqrt(x)
    return z


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


# Головна функція програми
def main():
    # Вводимо число x
    x = input_number("Введіть значення x: ")
    # Обчислюємо z
    z = calculate_z(x)
    # Виводимо результат
    print(f"Результат обчислення z: {z}")

    # Вводимо число n
    n = input_number("Введіть число n: ")
    # Знаходимо суму його цифр
    digit_sum = sum_of_digits(n)
    # Виводимо результат
    print(f"Сума цифр числа {n}: {digit_sum}")


# Викликаємо головну функцію програми
if __name__ == "__main__":
    main()
