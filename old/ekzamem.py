from selenium import webdriver
import time

answers = []
rez = []

PATH = 'C:\Program Files\selenium\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get('https://findhow.org/1057-onlayn-test-po-pravilam-dorozhnogo-dvizheniya-rk.html')
time.sleep(5)
driver.find_elements_by_class_name('button-text')[0].click()
time.sleep(5)
driver.find_elements_by_class_name('but-blocks-table')[12].click()
time.sleep(5)
driver.find_elements_by_class_name('but-blocks-block-test-text')[0].click()
time.sleep(5)
for i in range(149):
    driver.find_elements_by_id('next-button')[0].click()
time.sleep(1)
driver.find_elements_by_id('endtest-button')[0].click()
time.sleep(5)

for i in range(149):
    answers.append(driver.find_elements_by_class_name('detail-result-div')[i].text)

for i in range(len(answers)):
    rez.append(answers[i].split('\n')[4][14:])

print(rez)

driver.get('https://findhow.org/1057-onlayn-test-po-pravilam-dorozhnogo-dvizheniya-rk.html')

time.sleep(5)
driver.find_elements_by_class_name('button-text')[0].click()
time.sleep(5)
driver.find_elements_by_class_name('but-blocks-table')[12].click()
time.sleep(5)
driver.find_elements_by_class_name('but-blocks-block-test-text')[0].click()
time.sleep(5)

for i in range(149):
    driver.find_elements_by_class_name('css-radiolabel')[[z.text for z in driver.find_elements_by_class_name('css-radiolabel')].index(rez[i])].click()
    time.sleep(0.1)
    print(rez[i])
    driver.find_elements_by_id('next-button')[0].click()
    time.sleep(1)
