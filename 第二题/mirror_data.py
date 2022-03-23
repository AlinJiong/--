from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import xlwt
mirror_data = xlwt.Workbook(encoding='utf-8')
sheet = mirror_data.add_sheet('mirrordata', cell_overwrite_ok=True)
sheet.write(0, 0, '标签')
sheet.write(0, 2, 'mirror博主')
sheet.write(0, 1, 'mirror博主链接')
sheet.write(0, 3, '一句话简介')
sheet.write(0, 4, '网址链接')

s = Service(executable_path = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://glowing-october-bb2.notion.site/Mirror-fd9f8e8af755430d8f7dea78a65caf9a")

driver.implicitly_wait(15)
js="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
i = 2
a = b = c = d = e = True
while a or b or c or d or e:
    try:
        a = driver.find_element(By.XPATH, '//tr[{}]/td[1]/div/div'.format(i)).text
    except:
        a = None
    try:
        b = driver.find_element(By.XPATH, '//tr[{}]/td[2]/div/div/a'.format(i)).get_attribute('href')

    except:
        b = None
    try:
        c = driver.find_element(By.XPATH, '//tr[{}]/td[2]/div/div'.format(i)).text
    except:

        c = None
    try:
        d = driver.find_element(By.XPATH, '//tr[{}]/td[3]/div/div'.format(i)).text
    except:
        d = None
    try:
        e = driver.find_element(By.XPATH, '//tr[{}]/td[4]/div/div/a/span'.format(i)).text
    except:
        e = None
    sheet.write(i-1, 0, a)
    sheet.write(i-1, 1, b)
    sheet.write(i-1, 2, c)
    sheet.write(i-1, 3, d)
    sheet.write(i-1, 4, e)
    i = i+1

mirror_data.save(r"E:\新桌面\第二题\mirrordata表.xls")
driver.close()
