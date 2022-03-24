import json, requests, time, random
import pandas as pd


def get_data():
    urls = [
        'https://api.yitaifang.com/index/accounts/?page=' + str(x)
        for x in range(1, 11)
    ]
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
    }
    res = []
    for url in urls:
        response = requests.get(url, headers=headers)
        time.sleep(random.randint(3, 5))
        response_dic = json.loads(response.text)
        data = response_dic['data']['result']
        for item in data:
            _temp_list = [
                item['address'], item['balance'], item['percentage'],
                item['transactions']
            ]
            res.append(_temp_list)

    return res


data = get_data()

columns = ['地址', '余额', '占比', '交易笔数']
res = pd.DataFrame(columns=columns, data=data)
res.to_csv('eth.csv', encoding='utf-8')
