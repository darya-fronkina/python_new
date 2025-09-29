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




