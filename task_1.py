# Лабораторная №1: Первичная инициализация
# Курс: Основы теории систем
# Студент: Петров Артём Михайлович 

def get_system_info():
    """
    Эта функция должна вернуть словарь с информацией о вашей "системе".
    """
    # TODO: Заполните словарь вашими реальными данными
    system_info = {
        "student_name": "Петров Артём Михайлович",
        "academic_group": "ИВТИИбд-14",
        "github_link": "https://github.com/deside322"
    }
    return system_info

# Вывод информации для проверки
if __name__ == "__main__":
    info = get_system_info()
    print("Информация о системе:")
    for key, value in info.items():
        print(f"- {key}: {value}")
   git commit -m "Init task 1"
