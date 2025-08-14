import requests
import sys
import json


while True:
    try:
        bitcoins_to_buy = float(sys.argv[1])
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        object = response.json()
        bpi_dict = object["bpi"]
        USD_dict = bpi_dict["USD"]
        total_amount_to_buy = bitcoins_to_buy * USD_dict["rate_float"]
        print(f"${total_amount_to_buy:,.4f}")
        break
    except IndexError:
        sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")
    except requests.RequestException:
        pass
