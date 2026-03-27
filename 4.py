def make_payment(s):
    """
    The function checks the ability to pay a monthly payment on a credit card
    """
    credit_limit = 1000
    min_payment = 20
    
    if not isinstance(s, (int, float)):
        print("Ошибка: Сумма платежа должна быть числом")
        print("Повторить попытку")
        return

    if s < 0:
        print("Ошибка: Сумма платежа не может быть отрицательной")
        print("Повторить попытку")
        return

    if s < min_payment:
        print(f"Ошибка: Минимальный платеж составляет {min_payment}")
        print("Повторить попытку")
        return

    if s > credit_limit:
        print(f"Ошибка: Сумма платежа превышает кредитный лимит {credit_limit}")
        print("Повторить попытку")
        return
    
    print("Успех")
    
make_payment('двадцать')
