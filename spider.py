import json, requests, time, csv


def stamp2time(timestamp):
    time_local = time.localtime(int(timestamp))
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return dt


def url2csv(url, csvfile = 'btc.csv'):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    respone = requests.get(url=url, headers=headers)
    respone_dic = json.loads(respone.text)
    data = respone_dic['data']['btc']['list']

    with open(csvfile, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['排名', '地址', '余额', '交易总数', '最新转账余额', '最新转账时间'])

        for item in data:
            item_dic = item
            writer.writerow([
                item_dic['id'], item_dic['address'], item_dic['balance'],
                item_dic['total_tx_count'], item_dic['last_tx_balance_diff'],
                stamp2time(item_dic['last_tx_timestamp'])
            ])



urls = [
    'https://explorer.api.btc.com/stats/address/rich/top?app_a=S2Q4QUljMHEwNzNoMAI5XdXXMAgwqxia4P8VScnvddXEG5EguXvUEXk4ccTC&app_b=Kd8AIc0q073h0&nonce=DJI22151IXIC7512&timestamp=1648084959&coins=btc&max_count=1000&page=1&page_size=100&sign=jhT8VdPSMluw/H8wlICLhX/TfsJ4Y2tGa//GZVoeXuY=',
    'https://explorer.api.btc.com/stats/address/rich/top?app_a=S2Q4QUljMHEwNzNoMAI5XdXXMAgwqxia4P8VScnvddXEG5EguXvUEXk4ccTC&app_b=Kd8AIc0q073h0&nonce=DJI22151IXIC7512&timestamp=1648084974&coins=btc&max_count=1000&page=2&page_size=100&sign=JnDZ8559xDNDDKayVwfli1CXSUY5svHW2cDVWDFpM6U=',
    'https://explorer.api.btc.com/stats/address/rich/top?app_a=S2Q4QUljMHEwNzNoMAI5XdXXMAgwqxia4P8VScnvddXEG5EguXvUEXk4ccTC&app_b=Kd8AIc0q073h0&nonce=DJI22151IXIC7512&timestamp=1648084993&coins=btc&max_count=1000&page=3&page_size=100&sign=n+f4rMDkUjcB7BuU+Og8bjt3778oOTucT699Pr8AYak=',
    'https://explorer.api.btc.com/stats/address/rich/top?app_a=S2Q4QUljMHEwNzNoMAI5XdXXMAgwqxia4P8VScnvddXEG5EguXvUEXk4ccTC&app_b=Kd8AIc0q073h0&nonce=DJI22151IXIC7512&timestamp=1648085005&coins=btc&max_count=1000&page=4&page_size=100&sign=aYezSf0oKF6TZnwbLam7GBtGbWKsly3kQPv6MmrojG4=',
    'https://explorer.api.btc.com/stats/address/rich/top?app_a=S2Q4QUljMHEwNzNoMAI5XdXXMAgwqxia4P8VScnvddXEG5EguXvUEXk4ccTC&app_b=Kd8AIc0q073h0&nonce=DJI22151IXIC7512&timestamp=1648085019&coins=btc&max_count=1000&page=5&page_size=100&sign=yCtgR6ZfkfqdzOaQfCGGgfEox4eh9ILhfKfu1ypPvXk=',
    'https://explorer.api.btc.com/stats/address/rich/top?app_a=S2Q4QUljMHEwNzNoMAI5XdXXMAgwqxia4P8VScnvddXEG5EguXvUEXk4ccTC&app_b=Kd8AIc0q073h0&nonce=DJI22151IXIC7512&timestamp=1648085029&coins=btc&max_count=1000&page=6&page_size=100&sign=5AY08q2KWrTc2YGWZibCNbSvefnkzaSlTzFj5sbNOYY=',
    'https://explorer.api.btc.com/stats/address/rich/top?app_a=S2Q4QUljMHEwNzNoMAI5XdXXMAgwqxia4P8VScnvddXEG5EguXvUEXk4ccTC&app_b=Kd8AIc0q073h0&nonce=DJI22151IXIC7512&timestamp=1648085040&coins=btc&max_count=1000&page=7&page_size=100&sign=TfaYEGJOmC+dQOyPZMTVne3UA2D9AZDUNCXNt4eQpDs=',
    'https://explorer.api.btc.com/stats/address/rich/top?app_a=S2Q4QUljMHEwNzNoMAI5XdXXMAgwqxia4P8VScnvddXEG5EguXvUEXk4ccTC&app_b=Kd8AIc0q073h0&nonce=DJI22151IXIC7512&timestamp=1648085051&coins=btc&max_count=1000&page=8&page_size=100&sign=Go19RQX+u2M9qyOF9ecu1q/S6fyjarNVI6aVkCtswEk=',
    'https://explorer.api.btc.com/stats/address/rich/top?app_a=S2Q4QUljMHEwNzNoMAI5XdXXMAgwqxia4P8VScnvddXEG5EguXvUEXk4ccTC&app_b=Kd8AIc0q073h0&nonce=DJI22151IXIC7512&timestamp=1648085065&coins=btc&max_count=1000&page=9&page_size=100&sign=GOOZGa7sEQb0lr5MXULz93ZrzWH1iTCXZR8nctjmz+A=',
    'https://explorer.api.btc.com/stats/address/rich/top?app_a=S2Q4QUljMHEwNzNoMAI5XdXXMAgwqxia4P8VScnvddXEG5EguXvUEXk4ccTC&app_b=Kd8AIc0q073h0&nonce=DJI22151IXIC7512&timestamp=1648085076&coins=btc&max_count=1000&page=10&page_size=100&sign=PF4uKBQJKOS4ILV3AZYkW0CSuwWINTG+lEUs3JxjJkI='
]


for i in range(len(urls)):
    url2csv(urls[i], str(i)+'.csv')