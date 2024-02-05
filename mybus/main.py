import requests

url = "https://cdu-rest-api.tha.kz/position/list?routes=20518233"

payload={}
headers = {
  'authority': 'cdu-rest-api.tha.kz',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'ru-RU,ru;q=0.9,en;q=0.8,kk;q=0.7',
  'origin': 'https://citybus.tha.kz',
  'referer': 'https://citybus.tha.kz/',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102"',
  'sec-ch-ua-mobile': '?1',
  'sec-ch-ua-platform': '"Android"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
  'x-auth-token': '03AFcWeA6rgXOl8o_I0IBMpO0_TJ862keokVrfi7thvK6FKxWcQR9dy3V9C8nzldgowWtzrHyhG5UkVSZJhNiOYyLbSCcZI2R_kTREao_cFH5CdNgaoWdRukNC7s8aydICCOCqDvO0fG-JfzCpBIviwwLce86ysx5Tr116ah0MxIXxaZuWGSujsQvjHMbXHxy1Hi4wylLs5xpFWumpFuJXLo5BuB1vfUo6mr_7VjTfumNVRgZo_Kg1a3sPI3XQxQb9CJPH_APgIzjp8H1vKU9A1oMN4Xy8ziUMoeH9PhRP--JmQi5SbHVzIZAirqbGiXyrE1V3Puv1z9APFM-OnBK6qxmvd2ODsDUXx7PCARWehljQ0gBsWK40YgDC3WDEXoDmv1TyDuetS-Lkv5C02Vbvcpczm-QbuP_gFe5d8pTbnGKChRfBMg0r2MmQay-QzF-mga3-D-xdoIkgwVvDxXxWpf8hwm9tlziINsFEhyrZYbWxm7nuUQh0u-2_l3wJOKPnvTmFw8zit2zXH6vnrc8m38S8-DL_MPyiR-mPCil9pRvt_TAGSJ0BZ1s',
  'x-visitor-id': '92e071aec23eed6c4ca2fd81385857c5'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
