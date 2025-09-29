def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер карты по формату XXXX XX** **** XXXX

    Args:
        card_number (int): Номер карты в виде числа

    Returns:
        str: Замаскированный номер карты
    """
    # Преобразуем номер в строку и удаляем возможные пробелы
    card_str = str(card_number).replace(" ", "")

    # Проверяем, что номер карты содержит 16 цифр
    if len(card_str) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

    # Разбиваем номер на части и формируем маску
    part1 = card_str[:4]  # первые 4 цифры
    part2 = card_str[4:6]  # следующие 2 цифры
    part3 = "**"  # маскируем следующие 4 цифры
    part4 = "****"  # маскируем следующие 4 цифры
    part5 = card_str[12:]  # последние 4 цифры

    return f"{part1} {part2} {part3} {part4} {part5}"


def get_mask_account(account_number: int) -> str:
    """
    Маскирует номер счета по формату **XXXX

    Args:
        account_number (int): Номер счета в виде числа

    Returns:
        str: Замаскированный номер счета
    """
    # Преобразуем номер в строку и удаляем возможные пробелы
    account_str = str(account_number).replace(" ", "")

    # Проверяем, что номер счета содержит минимум 4 цифры
    if len(account_str) < 4:
        raise ValueError("Номер счета должен содержать минимум 4 цифры")

    # Берем последние 4 цифры и добавляем ** в начало
    return f"**{account_str[-4:]}"