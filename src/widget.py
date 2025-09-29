from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data_string: str) -> str:
    """
    Маскирует номер карты или счета в строке, содержащей тип и номер.

    Args:
        data_string (str): Строка с типом и номером карты/счета, например:
                          "Visa Platinum 7000792289606361"
                          "Счет 73654108430135874305"

    Returns:
        str: Строка с замаскированным номером карты или счета

    Raises:
        ValueError: Если строка не содержит номер или номер невалидный
    """
    # Разделяем строку на слова
    parts = data_string.split()

    if len(parts) < 2:
        raise ValueError("Строка должна содержать тип и номер карты/счета")

    # Тип - все слова кроме последнего
    data_type = " ".join(parts[:-1])
    # Номер - последнее слово
    number_str = parts[-1]

    # Проверяем, что номер состоит только из цифр
    if not number_str.isdigit():
        raise ValueError("Номер должен содержать только цифры")

    # Определяем тип данных (карта или счет) и применяем соответствующую маскировку
    if data_type.lower() == "счет":
        # Для счета
        masked_number = get_mask_account(int(number_str))
    else:
        # Для карты
        masked_number = get_mask_card_number(int(number_str))

    return f"{data_type} {masked_number}"

def get_date(date_string: str) -> str:
    """
    Преобразует дату из формата "2024-03-11T02:26:18.671407" в формат "ДД.ММ.ГГГГ"

    Args:
        date_string (str): Дата в формате "2024-03-11T02:26:18.671407"

    Returns:
        str: Дата в формате "ДД.ММ.ГГГГ"

    Raises:
        ValueError: Если входная строка имеет неверный формат
    """
    # Разделяем строку по 'T' чтобы отделить дату от времени
    parts = date_string.split('T')

    if len(parts) < 1:
        raise ValueError(f"Неверный формат даты: {date_string}")

    date_part = parts[0]

    # Разделяем дату на год, месяц и день
    date_components = date_part.split('-')

    if len(date_components) != 3:
        raise ValueError(f"Неверный формат даты: {date_string}")

    year, month, day = date_components

    # Проверяем, что все компоненты являются числами
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        raise ValueError(f"Неверный формат даты: {date_string}")

    # Форматируем в нужный вид
    return f"{day}.{month}.{year}"


