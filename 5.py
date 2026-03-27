def calculate_card_value():
    """The function asks the user for the
card's value and returns the cash equivalent,
taking into account bonuses"""

    card_price = input("Введите стоимость карты (5, 10, 25, 50, 100): ")
    
    try:
        card_price = int(card_price)
    except ValueError:
        print("Ошибка: Введите число")
        return None

    if card_price == 5 or card_price == 10:
        bonus = 0
        total_value = card_price + bonus
        print(f"Стоимость карты: {card_price}, бонус: {bonus}")
        return total_value
    
    elif card_price == 25:
        bonus = 3
        total_value = card_price + bonus
        print(f"Стоимость карты: {card_price}, бонус: {bonus}")
        return total_value
    
    elif card_price == 50:
        bonus = 8
        total_value = card_price + bonus
        print(f"Стоимость карты: {card_price}, бонус: {bonus}")
        return total_value
    
    elif card_price == 100:
        bonus = 20
        total_value = card_price + bonus
        print(f"Стоимость карты: {card_price}, бонус: {bonus}")
        return total_value
    
    else:
        print("Ошибка: Допустимые значения: 5, 10, 25, 50, 100")
        return None

calculate_card_value()
