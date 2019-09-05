from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Находим х и вычисляем функцию
    x = browser.find_element_by_id("treasure").get_attribute("valuex")
    y = calc(x)   

    browser.find_element_by_id('answer').send_keys(y)

    # Отмечаем чекбокс
    browser.find_element_by_id('robotCheckbox').click()
    
    #Отмечаем радиокнопку
    browser.find_element_by_id('robotsRule').click()

    #Жмем Submit
    browser.find_element_by_css_selector("button.btn").click()
   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


#
