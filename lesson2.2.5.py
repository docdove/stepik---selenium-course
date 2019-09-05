from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Находим х и вычисляем функцию
    x = browser.find_element_by_id('input_value').text
    #print(x)
    y = calc(x)

    browser.find_element_by_id('answer').send_keys(y)

    #Отмечаем чекбокс
    browser.find_element_by_id('robotCheckbox').click()
    
    #from selenium.webdriver.support.ui import Select
    #select = Select(browser.find_element_by_tag_name('select'))
    #select.select_by_visible_text(z)

    button = browser.find_element_by_css_selector('button.btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    #Отмечаем радиокнопку
    browser.find_element_by_id('robotsRule').click()

    #Жмем Submit
    #button = browser.find_element_by_css_selector('button.btn')
    button.click()
   
finally:
    #ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    #закрываем браузер после всех манипуляций
    browser.quit()


#
