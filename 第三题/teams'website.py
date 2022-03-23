from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import xlwt

pws = xlwt.Workbook(encoding='utf-8')

sheet = pws.add_sheet('mirrordata', cell_overwrite_ok=True)
sheet.write(0, 1, '图片链接')
sheet.write(0, 2, '备注')
sheet.write(0, 0, '网址')

s = Service(executable_path=r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://labs.binance.com/")

driver.implicitly_wait(15)
js = "var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
i = 1
a = b = c = True
while a or b or c:
    try:
        a = driver.find_element(By.XPATH, '//*[@id="section-portfolio"]/div/div[2]/div/div[{}]/a'.format(i)).get_attribute('href')
        a = str(a)

    except:
        a = None
    try:
        b = driver.find_element(By.XPATH, '//*[@id="section-portfolio"]/div/div[2]/div/div[{}]/a/img'.format(i)).get_attribute('src')
        b = str(b)

    except:
        b = None
    try:
        c = driver.find_element(By.XPATH, '//*[@id="section-portfolio"]/div/div[2]/div/div[{}]/a/img'.format(i)).get_attribute('alt')
        c = str(c)

    except:
        c = None


    sheet.write(i, 0, a)
    sheet.write(i, 1, b)
    sheet.write(i, 2, c)

    i = i + 1

pws.save(r"./teams_websitedata.xls")
driver.close()