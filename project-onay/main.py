import requests
import re
from requests.exceptions import SSLError

requests.packages.urllib3.disable_warnings()

def fetch_card_info(pan):
    info_url = 'https://cabinet.onay.kz/check'
    # Делаем POST-запрос на получение информации о карточке
    response = requests.post(info_url, verify=False)

    return response


card_info = fetch_card_info('9643908503312936614')
print(card_info)
