import datetime

DIGITS = {
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

DIGIT_HEIGHT = 5


def print_large_number(num_str: str, spacing: int = 2) -> None:
    """Выводит число крупными цифрами из звёздочек."""
    lines = [""] * DIGIT_HEIGHT

    for char in num_str:
        if char not in DIGITS:
            for i in range(DIGIT_HEIGHT):
                lines[i] += " " * (5 + spacing)
            continue

        for i in range(DIGIT_HEIGHT):
            lines[i] += DIGITS[char][i] + " " * spacing

    print()
    for line in lines:
        print(line)
    print()


def print_separator(char: str = "=", length: int = 50) -> None:
    """Выводит разделительную линию."""
    print(char * length)


def print_header(text: str) -> None:
    """Выводит заголовок с разделителями."""
    print_separator()
    print(f"  {text}")
    print_separator()


# ФУНКЦИИ РАБОТЫ С ДАТАМИ


def get_day_of_week(day: int, month: int, year: int) -> str:
    """Определяет день недели для заданной даты."""
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


def is_leap_year(year: int) -> bool:
    """Проверяет, является ли год високосным."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def calculate_age(day: int, month: int, year: int) -> int:
    """Вычисляет возраст пользователя в полных годах."""
    today = datetime.date.today()
    birth_date = datetime.date(year, month, day)

    if birth_date > today:
        raise ValueError("Дата рождения не может быть в будущем!")

    age = today.year - birth_date.year

    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age


def validate_date_input(
    day_str: str, month_str: str, year_str: str
) -> tuple[int, int, int]:
    """Проверяет и преобразует ввод пользователя в корректную дату."""
    try:
        day = int(day_str)
        month = int(month_str)
        year = int(year_str)
    except ValueError:
        raise ValueError("Все значения должны быть целыми числами!")

    if not (1 <= day <= 31):
        raise ValueError(f"День должен быть от 1 до 31 (введено: {day})")

    if not (1 <= month <= 12):
        raise ValueError(f"Месяц должен быть от 1 до 12 (введено: {month})")

    today_year = datetime.date.today().year
    if not (1 <= year <= today_year):
        raise ValueError(f"Год должен быть от 1 до {today_year}")

    try:
        datetime.date(year, month, day)
    except ValueError:
        raise ValueError(f"Такой даты не существует: {day}.{month}.{year}")

    return day, month, year


# ОСНОВНАЯ ЛОГИКА


def get_user_input() -> tuple[int, int, int]:
    """Запрашивает и валидирует ввод даты от пользователя."""
    while True:
        try:
            print("\nВведите дату рождения:")
            day_input = input("  День (1-31): ").strip()
            month_input = input("  Месяц (1-12): ").strip()
            year_input = input("  Год (например, 1990): ").strip()

            return validate_date_input(day_input, month_input, year_input)

        except ValueError as e:
            print(f"\n  ⚠ Ошибка: {e}")
            print("  Попробуйте ещё раз.\n")


def display_results(day: int, month: int, year: int) -> None:
    """Выводит все результаты анализа даты."""
    print_header("РЕЗУЛЬТАТЫ АНАЛИЗА")

    # День недели
    weekday = get_day_of_week(day, month, year)
    print(f"  День недели: {weekday}")

    # Високосность
    if is_leap_year(year):
        print(f"  Год {year} — високосный")
    else:
        print(f"  Год {year} — обычный")

    # Возраст
    try:
        age = calculate_age(day, month, year)
        # Склонение "год/года/лет"
        last_two = age % 100
        last_one = age % 10
        if 11 <= last_two <= 14:
            age_word = "лет"
        elif last_one == 1:
            age_word = "год"
        elif 2 <= last_one <= 4:
            age_word = "года"
        else:
            age_word = "лет"
        print(f"  Ваш возраст: {age} {age_word}")
    except ValueError as e:
        print(f"  Ошибка: {e}")

    # Электронное табло
    print_header("ДАТА РОЖДЕНИЯ НА ЭЛЕКТРОННОМ ТАБЛО")
    date_string = f"{day:02d}{month:02d}{year}"
    print(f"  Формат ДДММГГГГ: {date_string}")
    print_large_number(date_string)


# ГЛАВНЫЙ ЦИКЛ


def main() -> None:
    """Основная функция программы."""
    print_header("ПРОГРАММА АНАЛИЗА ДАТЫ РОЖДЕНИЯ")
    print("  Введите дату рождения, чтобы узнать день недели,")
    print("  високосность года, возраст и увидеть дату на табло.")

    while True:
        # 1. Ввод данных
        day, month, year = get_user_input()

        # 2. Вывод результатов (ГАРАНТИРОВАННО!)
        display_results(day, month, year)

        # 3. Только ПОСЛЕ вывода спрашиваем о продолжении
        print()
        print_separator("-", 50)
        print("  Введите 'да' для новой проверки или 'нет' для выхода")
        print_separator("-", 50)

        choice = input("  Ваш выбор: ").strip().lower()

        # Если ввели "нет", "н", "no", "n", "exit", "выход" — выходим
        if choice in ("нет", "н", "no", "n", "exit", "выход", "в", "0", "quit", "q"):
            print()
            print_separator()
            print("  До свидания!")
            print_separator()
            break

        # Иначе — продолжаем (и любой другой ответ тоже продолжает)
        print("\n" + "=" * 50)
        print("  НОВАЯ ПРОВЕРКА")
        print("=" * 50)


if __name__ == "__main__":
    main()
