def calculate_nights_total(number_of_nights, night_price):
    """
    >>> calculate_nights_total(5, 100)
    500
    >>> calculate_nights_total(0, 200)
    0
    """
    if number_of_nights <= 0 or night_price <= 0:
        return 0
    return number_of_nights * night_price


def add_city_tax(number_of_nights, night_price, city_tax):
    """
    >>> add_city_tax(5, 100, 200)
    700
    >>> add_city_tax(0, 200, 200)
    0
    >>> add_city_tax(2, 200, 0)
    400
    """
    if calculate_nights_total(number_of_nights, night_price) <= 0:
        return 0
    return calculate_nights_total(number_of_nights, night_price) + city_tax


def main():
    number_of_nights = int(input("Введіть кількість ночей: "))
    night_price = int(input("Введіть ціну за ніч: "))
    city_tax = int(input("Введіть міський податок: "))
    hotel_accommodation_cost = add_city_tax(number_of_nights, night_price, city_tax)
    print(f"Ціна проживання в готелі становить: {hotel_accommodation_cost}")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
