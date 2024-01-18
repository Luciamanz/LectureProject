import bs4
import requests
from . import models

COUNTRY_CURRENCIES_SYMBOLS_URL = "https://thefactfile.org/countries-currencies-symbols/"


def get_currencies() -> list:
    response = requests.get(COUNTRY_CURRENCIES_SYMBOLS_URL)
    if not response.status_code == 200:
        return []

    soup = bs4.BeautifulSoup(response.content, 'html.parser')

    currencies = set()
    for line in soup.find_all('tr'):
        try:
            td = line.find_all('td')

            currency = td[2].get_text().strip()
            iso = td[3].get_text().strip()
        except (AttributeError, IndexError):
            continue

        currencies.add((currency, iso))

    return sorted(currencies)


def add_currencies_to_db(currencies: list) -> None:
    #for obj in models.Currency.objects.all():
        #obj.delete()

    for currency in currencies:
        iso = currency[1]
        long_name = currency[0]

        c = models.Currency.objects.filter(iso=iso).first()
        if c is None:
            c = models.Currency(
                iso=currency[1],
                long_name=currency[0]
            )
        else:
            c.iso = iso
            c.long_name = long_name

        c.save()
