import json
from common.send import send
from common.telegram import n
def save(file):
    a = json.dumps(file)
    print(a)
    with open(r'common\files\data.json', 'r') as f:
        text = f.read().replace('\n','')
        if text != '':
            pass
            #with open(r'common\files\ef.text', 'a') as fi:
            #    fi.write(f'{text}\n')
    with open(r'common\files\data.json', 'w') as fl:
        fl.write(f'{a}\n')
    send(a)
    n()
