import json, time
import requests


def stamp2time(timestamp):
    time_local = time.localtime(int(timestamp))
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return dt


def get_eth_largetxs_data():
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
    }

    res = requests.get('https://api.yitaifang.com/index/largetxs/?page=1',
                       headers=headers)

    res_dic = json.loads(res.text)

    data = res_dic['data']['result']

    _data = []
    for item in data:
        #交易时间，区块高度，发送方，接受方，币种，时价，转账量，价值
        txTime = stamp2time(item['timestamp'])
        blockNumber = item['blockNumber']
        txFrom = item['from']
        txTo = item['to']

        try:
            txType = item['internalTransaction'][0]['symbol']
        except:
            txType = "ETH"

        try:
            txTimePrice = item['internalTransaction'][0]['price']
        except:
            txTimePrice = item['price']

        try:
            txNum = item['internalTransaction'][0]['value']
        except:
            txNum = item['value']

        txValue = float(txNum) * float(txTimePrice)

        _data.append(
            [txTime, blockNumber, txFrom, txTo, txType, txTimePrice, txValue])

    return _data