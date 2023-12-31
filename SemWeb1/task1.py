# С использованием фреймворка pytest
# написать тест операции checkText SOAP API https://speller.yandex.net/services/spellservice?WSDL
# Тест должен использовать DDT и проверять наличие определенного верного слова в списке предложенных
# исправлений к определенному неверному слову.
# Слова должны быть заданы через фикстуры в conftest.py, адрес wsdl должен быть вынесен в config.yaml.
# Методы работы с SOAP должны быть вынесены в отдельную библиотеку.


import yaml
from zeep import Client, Settings


with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    wsdl = data['wsdl']

settings = Settings(strict=False)
client = Client(wsdl=wsdl, settings=settings)


def check_text(text: str) -> list[str]:
    resp = client.service.checkText(text)
    return resp[0]['s']
