def f1():

    class Restaurant():
        # Метод __init__ инициализирует атрибуты restaurant_name и cuisine_type
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name  # Имя ресторана
            self.cuisine_type = cuisine_type  # Тип кухни

        # Метод describe_restaurant выводит информацию о ресторане
        def describe_restaurant(self):
            print('Имя ресторана:', self.restaurant_name)
            print('Тип кухни:', self.cuisine_type)

        # Метод open_restaurant выводит сообщение о том, что ресторан открыт
        def open_restaurant(self):
            print('Ресторан открыт')

    # Создаем экземпляр класса Restaurant с именем
    newRestaurant = Restaurant('Банда Панд', 'китайская')
    # Вызываем метод describe_restaurant для вывода информации о ресторане
    newRestaurant.describe_restaurant()
    # Вызываем метод open_restaurant для вывода сообщения о том, что ресторан открыт

f1()
def f2():

    class Restaurant():
        # Метод __init__ инициализирует атрибуты restaurant_name и cuisine_type
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name  # Имя ресторана
            self.cuisine_type = cuisine_type  # Тип кухни

        # Метод describe_restaurant выводит информацию о ресторане
        def describe_restaurant(self):
            print('Имя ресторана:', self.restaurant_name)
            print('Тип кухни:', self.cuisine_type)

        # Метод open_restaurant выводит сообщение о том, что ресторан открыт
        def open_restaurant(self):
            print('Ресторан открыт')

    # Создаем экземпляры класса Restaurant с разными значениями
    restaurant1 = Restaurant('Хлеб на обед', "Выпечка")
    restaurant2 = Restaurant("Буено", "итальянская")
    restaurant3 = Restaurant('Банда Падн', "семейная")

    # Выводим информацию о каждом ресторане
    restaurant1.describe_restaurant()
    print('\n')
    restaurant2.describe_restaurant()
    print('\n')
    restaurant3.describe_restaurant()

f2()


def f3():
    class Restaurant():
        # Метод __init__ инициализирует атрибуты restaurant_name, cuisine_type и rating
        def __init__(self, restaurant_name, cuisine_type, rating):
            self.restaurant_name = restaurant_name  # Имя ресторана
            self.cuisine_type = cuisine_type  # Тип кухни
            self.rating = rating  # Рейтинг

        # Метод describe_restaurant выводит информацию о ресторане, включая рейтинг
        def describe_restaurant(self):
            print('Имя ресторана: ', self.restaurant_name)
            print('Тип кухни: ', self.cuisine_type)
            print('Рейтинг: ', self.rating)

        # Метод open_restaurant выводит сообщение о том, что ресторан открыт
        def open_restaurant(self):
            print('Ресторан открыт')

        # Метод update_rating позволяет обновить рейтинг ресторана
        def update_rating(self, new_rating):
            self.rating = new_rating

    # Создаем экземпляры класса Restaurant с разными значениями
    restaurant1 = Restaurant('Хлеб на обед', "Выпечка", 4.7)
    restaurant2 = Restaurant("Буено", "Итальянская", 5)
    restaurant3 = Restaurant('Банда Панд', "Семейная", 3.9)

    # Выводим информацию о каждом ресторане
    restaurant1.describe_restaurant()
    print('\n')
    restaurant2.describe_restaurant()
    print('\n')

f3() 






