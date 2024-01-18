from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Currency(models.Model):
    iso = models.CharField(max_length=3)
    long_name = models.CharField(max_length=50)


    def __str__(self):
        return f'{self.iso} {self.long_name}'


class Holdings(models.Model):
    currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
    )
    value = models.FloatField(default=0.0)
    buy_date = models.DateField()
#when related Currency deleted, delete this holding
    def __str__(self):
        return f'{self.currency.iso} {self.value} {self.buy_date}'

class Rate(models.Model):
    currency_one = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        related_name='currency_one_set',
    )
    currency_two = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        related_name='currency_two_set',
    )
    rate = models.FloatField(default = 1.0)
    last_update_time=models.DateTimeField()

    def __str__(self):
        return f'{self.currency_one} {self.currency_two} {self.rate} {self.last_update_time}'


class AccountHolder(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,

    )
    date_of_brith = models.DateField(),
    currencies_visited = models.ManyToManyField(
        Currency,
    )