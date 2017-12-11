""""A useful utility for querying openExchangeRate"""
__author__ = "Anir C"

# imports from Python standard libraries
import pandas as pd
import requests
import urllib.parse
from pandas.io.json import json_normalize


def import_ExchangeRate(toCurr,onDate):
    """Uses the openexchangerates API to look up FX rate information
    base -- the base currency (always USD)
    toCurr -- the currencies to be converted into USD(optional)
    """

    #set app code
    app_code = '09e66a35af4b4736b8ec7111ed699942'
    url= 'https://openexchangerates.org/api/latest.json?app_id='+ app_code + urllib.parse.urlencode({'&symbols':toCurr})
    try:
        fx_rate = requests.get(url).json()
    except:
        # failed api lookup
        raise ValueError("No exchange rate for the given currency or date could be found")
    rate = pd.DataFrame(fx_rate['rates'])

    return {'rates':rate}


def get_Currencies():


    #set app code
    app_code = '09e66a35af4b4736b8ec7111ed699942'
    url = 'https://openexchangerates.org/api/currencies.json?app_id=' + app_code

    try:
        curr = requests.get(url).json()
    except:
        # failed api lookup
        raise ValueError("No currencies could be found")

    return curr
