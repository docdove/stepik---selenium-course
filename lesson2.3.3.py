from selenium import webdriver
import time
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = 'http://suninjuly.github.io/alert_accept.html'
    filename = 'blanck.txt'
    browser = webdriver.Chrome()
    browser.get(link)

    #отправляемся в магическое приключение
    browser.find_element_by_css_selector('button.btn').click()

    browser.switch_to.alert.accept()

    #Находим х и вычисляем функцию
    x = browser.find_element_by_id('input_value').text
    y = calc(x)  

    browser.find_element_by_id('answer').send_keys(y) 

    #Заполняем необходимые поля
    #browser.find_element_by_name('firstname').send_keys('Firstname')
    #browser.find_element_by_name('lastname').send_keys('Lastname')
    #browser.find_element_by_name('email').send_keys('e@ma.il')

    #Определяемся с текущей директрорией
    #pathdir = os.getcwd()
    #Прикрепляем к ней имя файла и передаем все кнопке Прикрепить файл
    #file_path = os.path.join(pathdir, filename)
    #browser.find_element_by_id('file').send_keys(file_path)

    #Жмем победную кнопку
    browser.find_element_by_css_selector('button.btn').click()
    
    #time.sleep(1)
    print(browser.switch_to.alert.text.split(': ')[-1])
   
finally:
    #ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    #закрываем браузер после всех манипуляций
    browser.quit()


#
