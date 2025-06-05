# Функція для обробки строки:
# виділяє голосні, підраховує їх кількість, і відокремлює приголосні
def process_text(text):
    vowels = "aeiouAEIOUаеєиіїоуюяАЕЄИІЇОУЮЯ"  # Усі голосні літери англійської та української абетки
    vowel_chars = ''  # Результат для голосних
    consonant_chars = ''  # Результат для приголосних
    count = 0  # Лічильник голосних

    for char in text:
        if char.isalpha():  # Ігноруємо символи, що не є літерами
            if char in vowels:
                vowel_chars += char  # Додаємо до голосних
                count += 1  # Збільшуємо лічильник
            else:
                consonant_chars += char  # Додаємо до приголосних

    return (vowel_chars, count, consonant_chars)  # Повертаємо кортеж з голосними, їх кількістю і приголосними

# Приклад використання
result = process_text("Привіт, як справи?")
print(result)  # ('иіаяа', 6, 'Првткспрв')