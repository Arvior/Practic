import datetime

digits = {  # числовые данные в виде звёздочек
    "0": [" *** ", "*   *", "*   *", "*   *", " *** "],
    "1": ["  *  ", " **  ", "  *  ", "  *  ", " *** "],
    "2": [" *** ", "*   *", "   * ", "  *  ", "*****"],
    "3": [" *** ", "*   *", "   * ", "*   *", " *** "],
    "4": ["   * ", "  ** ", " * * ", "*****", "   * "],
    "5": ["*****", "*    ", "**** ", "    *", "**** "],
    "6": [" *** ", "*    ", "**** ", "*   *", " *** "],
    "7": ["*****", "   * ", "  *  ", " *   ", "*    "],
    "8": [" *** ", "*   *", " *** ", "*   *", " *** "],
    "9": [" *** ", "*   *", " ****", "    *", " *** "],
}


def print_large_number(num_str):  # Выводит число крупными цифрами из звёздочек
    lines = [""] * 5
    for ch in num_str:
        for i in range(5):
            lines[i] += digits[ch][i] + " "
    for line in lines:
        print(line)


def day_of_week(day, month, year):  # Возвращает название дня недели для заданной даты
    date = datetime.date(year, month, day)
    weekdays = [
        "Понедельник",
        "Вторник",
        "Среда",
        "Четверг",
        "Пятница",
        "Суббота",
        "Воскресенье",
    ]
    return weekdays[date.weekday()]


def is_leap_year(year):  # Определяет, является ли год високосным
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def calculate_age(day, month, year):  # Вычисляет возраст в годах на сегодняшний день
    today = datetime.date.today()
    birth_date = datetime.date(year, month, day)
    age = today.year - birth_date.year
    if (today.month, today.day) < (
        birth_date.month,
        birth_date.day,
    ):  # Если день рождения ещё не наступил в этом году
        age -= 1
    return age


def main():
    print("=== Программа для статических чисел ===\n")

    try:
        day = int(input("Введите день рождения (число): "))
        month = int(input("Введите месяц рождения (число): "))
        year = int(input("Введите год рождения (число): "))

        birth_date = datetime.date(year, month, day)  # Проверка корректности даты

        print("\n" + "=" * 40)

        weekday = day_of_week(day, month, year)  # День недели
        print(f" День недели: {weekday}")

        if is_leap_year(year):  # Високосный ли год
            print(" Год рождения был високосным")
        else:
            print(" Год рождения не был високосным")

        age = calculate_age(day, month, year)  # Возраст пользователя
        print(f" Ваш возраст: {age} лет")

        print(
            "\n ДАТА РОЖДЕНИЯ НА ЭЛЕКТРОННОМ ТАБЛО: "
        )  # Вывод даты на электронном табло
        date_str = f"{day:02d}{month:02d}{year}"
        print_large_number(date_str)

    except ValueError:
        print("\n Ошибка: введены некорректные данные! Убедитесь, что дата существует.")
    except Exception as e:
        print(f"\n Ошибка: {e}")


if __name__ == "__main__":
    main()
