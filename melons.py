"""Classes for melon orders."""
import random
from datetime import date 
import datetime
import time

class AbstractMelonOrder():

    def __init__(self, species, qty):

        self.species = species
        self.qty = qty
        self.shipped = False

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_base_price(self):
        self.get_total = random.randint(5, 9)
        


        return self.get_total

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()
        if self.species == 'christmas melon':
            base_price *= 1.5
        total = (1 + self.tax) * self.qty * base_price

        return total


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super().__init__(species, qty)
        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super().__init__(species, qty)
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

    def get_total(self):
        """Calculate price, including tax."""

        total = super().get_total()
        if self.qty < 10:
            total += 3
        return total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):


    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.tax = 0
        self.passed_inspection = False

    def mark_inspection(self, passed):

        self.passed_inspection = passed


# thisXMas    = datetime.date(2017,12,25)

# thisXMasDay = thisXMas.weekday()              # this will retuen an integer 0-6


print(date(2021,5,7).weekday())
print(date(2021,5,8).weekday())
print(date(2021,5,9).weekday())
print("Today's day index: ", date(date.today().year, date.today().month ,date.today().day).weekday()) # this will retuen an integer 0-6

print("Date now : ", time.localtime().tm_year, "/", time.localtime().tm_mon, "/", time.localtime().tm_mday)
print("Time now : ", time.localtime().tm_hour, ":", time.localtime().tm_min, ":", time.localtime().tm_sec)

order0 = InternationalMelonOrder("watermelon", 9, "AUS")
print(order0.get_total())
order0.mark_shipped()
order4 = InternationalMelonOrder("watermelon", 10, "AUS")
print(order4.get_total())
order4.mark_shipped()

order1 = DomesticMelonOrder("cantaloupe", 8)
print(order1.get_total())
order1.mark_shipped()
order3 = DomesticMelonOrder("christmas melon", 8)
print(order3.get_total())
order3.mark_shipped()

order5 = GovernmentMelonOrder("Honeydew", 9)
print(order5.get_total())
order5.mark_inspection(True)
print(order5.passed_inspection)