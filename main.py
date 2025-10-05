from src.widget import mask_account_card, get_date


card = 'Visa Platinum 8990922113665229'
account = 'Счет 73654108430135874305'
date = "2024-03-11T02:26:18.671407"


if __name__ == '__main__':
    print(mask_account_card(card))
    print(mask_account_card(account))
    print(get_date(date))