import requests
token = '6495698589:AAF8IrqRoPuEERHNFztOqnikDtxL_xDBU10'
def send(file):
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={5270716903}&text={'тест'}"
    print(requests.get(url).json())