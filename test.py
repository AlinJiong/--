import requests


response = requests.get('https://glowing-october-bb2.notion.site/Mirror-fd9f8e8af755430d8f7dea78a65caf9a')


with open('test.html', 'w') as f:
    f.write(response.text)