# Создаем класс для кофемашины, который умеет продавать (команда buy), его можно
# наполнить ингредиаентами (fill), снять все деньги (take) и вывести остатки
# ингредиентов и денег (remaining)


class CoffeeMachine:
    status = "Let's do some coffee!"

    def __init__(self, water=0, milk=0, beans=0, cups=0, money=0):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def __str__(self):
        return f'The coffee machine has:\n'\
               '{} of water\n'\
               '{} of milk\n'\
               '{} of coffee beans\n'\
               '{} of disposable cups\n'\
               '${} of money\n'\
               '{}'.format(self.water, self.milk,
                           self.beans, self.cups,
                           self.money, self.status)
    # Считыватель строк. Если введен 'back' - возвращает машину в исходное
    # положение

    def reader(self):
        command = input()
        if command == 'back':
            return self.what_to_do()
        return command
    # Исходное положение. Спрашиваем, что нужно сделать: купить, наполнить,
    # вывести деньги или показать остатки

    def what_to_do(self):
        while True:
            print('Write action (buy, fill, take, remaining, exit):')
            option = self.reader()
            if option == 'buy':
                my_coffee.buy()
            elif option == 'fill':
                my_coffee.fill()
            elif option == 'take':
                my_coffee.take()
            elif option == 'remaining':
                my_coffee.remaining()
            elif option == 'exit':
                break
    # Команда купить. Предлагает на выбор эспрессо, латте, капучино

    def buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, '
              '3 - cappuccino, back - to main menu:')
        coffee = self.reader()
        coffee = int(coffee)
        if coffee == 1:
            self.refresh_ingredients_buy(water=250, beans=16,
                                         cups=1, money=4)
        elif coffee == 2:
            self.refresh_ingredients_buy(water=350, milk=75, beans=20,
                                         cups=1, money=7)
        elif coffee == 3:
            self.refresh_ingredients_buy(water=200, milk=100, beans=12,
                                         cups=1, money=6)

    # Наполняем машину

    def fill(self):
        print('Write how many ml of water do you want to add:')
        water = int(self.reader())
        print('Write how many ml of milk do you want to add:')
        milk = int(self.reader())
        print('Write how many grams of coffee beans do you want to add:')
        beans = int(self.reader())
        print('Write how many disposable cups of coffee do you want to add:')
        cups = int(self.reader())
        self.refresh_ingredients_fill(water=water, milk=milk, beans=beans,
                                      cups=cups)
    # Забираем деньги

    def take(self):
        print('I gave you {}$'.format(self.money))
        self.money -= self.money
    # Выводим остатки

    def remaining(self):
        print('The coffee machine has:\n'
              '{} of water\n'
              '{} of milk\n'
              '{} of coffee beans\n'
              '{} of disposable cups\n'
              '${} of money'.format(self.water, self.milk,
                                    self.beans, self.cups,
                                    self.money))
        return
    # Метод для обновления ингредиентов после покупки (то есть мы убираем ингредиенты
    # и прибавляем деньги. Если ингредиентов недостаточно, выдает ошибку

    def refresh_ingredients_buy(self, water=0, milk=0, beans=0,
                                cups=0, money=0):
        if [self.water, self.milk, self.beans, self.cups] \
                < [water, milk, beans, cups]:
            print("Sorry, I can't make a Cup of coffee")
            return
        self.water -= water
        self.milk -= milk
        self.beans -= beans
        self.cups -= cups
        self.money += money
    # Обнволяем ингредиенты после наполнения (добавляем их)

    def refresh_ingredients_fill(self, water=0, milk=0, beans=0,
                                 cups=0):
        self.water += water
        self.milk += milk
        self.beans += beans
        self.cups += cups


if __name__ == '__main__':
    my_coffee = CoffeeMachine(water=400, milk=540, beans=120, cups=9,
                              money=550)
    my_coffee.what_to_do()
