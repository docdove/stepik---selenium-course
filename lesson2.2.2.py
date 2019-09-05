from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Находим х и вычисляем функцию
    x = int(browser.find_element_by_id('num1').text)
    #print(x)
    y = int(browser.find_element_by_id('num2').text)
    #print (y)
    z = str(x + y)
    #print (z)

    #browser.find_element_by_id('answer').send_keys(y)

    #Отмечаем чекбокс
    #browser.find_element_by_id('robotCheckbox').click()
    
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_visible_text(z)

    #Отмечаем радиокнопку
    #browser.find_element_by_id('robotsRule').click()

    #Жмем Submit
    button = browser.find_element_by_css_selector('button.btn')
    button.click()
   
finally:
    #ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    #закрываем браузер после всех манипуляций
    browser.quit()


#
