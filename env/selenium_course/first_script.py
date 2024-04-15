# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# link = "https://www.degreesymbol.net/"

# try:
#     browser = webdriver.Chrome()
#     browser.get(link)

#     # Find the element by link text "Degree Symbol In Math" and click on it
#     link_element = browser.find_element(By.LINK_TEXT, "https://www.degreesymbol.net/math")
#     link_element.click()

#     time.sleep(5)  # Adding a short delay for visibility

# finally:
#     time.sleep(12)
#     # Closes the browser after all manipulations
#     browser.quit()

# import math 
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# link = "https://easysmarthub.ru/contact/"

# try:
#     code_snippet = '''import math 
#     import time
#     from selenium import webdriver
#     from selenium.webdriver.common.by import By

#     link = "https://easysmarthub.ru/contact/"



#     browser = webdriver.Chrome()
#     browser.get(link)

#     # Fill out the form fields
#     name_input = browser.find_element(By.NAME, "your-name")
#     name_input.send_keys("Roman Kolosov")

#     email_input = browser.find_element(By.NAME, "your-email")
#     email_input.send_keys("roman.kolosov@inbox.ru")

#     subject_input = browser.find_element(By.NAME, "your-subject")
#     subject_input.send_keys("Selenium course from Erik")

#     message_input = browser.find_element(By.NAME, "your-message")
#     message_input.send_keys(code_snippet)
#     # message_input.send_keys("Hello, Erik")

#     # Check the checkbox for GDPR
#     gdpr_checkbox = browser.find_element(By.NAME, "gdpr")
#     gdpr_checkbox.click()

#     # Submit the form
#     submit_button = browser.find_element(By.CLASS_NAME, "default-btn")
#     submit_button.click()


#     time.sleep(120)  '''

#     browser = webdriver.Chrome()
#     browser.get(link)


#     name_input = browser.find_element(By.NAME, "your-name")
#     name_input.send_keys("Roman Kolosov")

#     email_input = browser.find_element(By.NAME, "your-email")
#     email_input.send_keys("roman.kolosov@inbox.ru")

#     subject_input = browser.find_element(By.NAME, "your-subject")
#     subject_input.send_keys("Selenium course from Erik")

#     message_input = browser.find_element(By.NAME, "your-message")
#     message_input.send_keys(code_snippet)



#     gdpr_checkbox = browser.find_element(By.NAME, "gdpr")
#     gdpr_checkbox.click()


#     # submit_button = browser.find_element(By.CLASS_NAME, "default-btn")
#     # submit_button.click()
#     submit_button = browser.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'default-btn')]")
#     submit_button.click()

# finally:
#     time.sleep(10)
#     browser.quit()

# #Webdriver - это и есть набор команд для управления браузером
# from selenium import webdriver
# #импортируем класс By , который позволяет выбрать способ поиска элемента
# from selenium.webdriver.common.by import By


# import time


# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements(By.TAG_NAME, 'input')
#     for i in elements:
#         i.send_keys("Привет")
#     buton = browser.find_element(By.TAG_NAME,'button')
#     buton.click()
# finally:
#     time.sleep(30)
#     browser.quit()


# #next lesson
# import math 
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By


# link = "http://suninjuly.github.io/registration2.html"
# browser = webdriver.Chrome()
# browser.get(link)
# time.sleep(1)

# # Fill out the input fields with asterisk (*)
# input_elements = browser.find_elements(By.CSS_SELECTOR, "input[required]")
# for element in input_elements:
#     element.send_keys("check")

# time.sleep(1)

# # button = browser.find_element(By.CSS_SELECTOR, 'type="submit"')
# # button.click()
# # time.sleep(5)
# # browser.quit()

# button = browser.find_element(By.CSS_SELECTOR, '[button type="submit"]')
# button.click()
# time.sleep(1)
# browser.quit()


#next lesson

# #Webdriver - это и есть набор команд для управления браузером
# from selenium import webdriver
# #импортируем класс By , который позволяет выбрать способ поиска элемента
# from selenium.webdriver.common.by import By
# import time


# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/registration2.html")
#     elements = browser.find_elements(By.TAG_NAME, 'input')
#     for i in elements:
#         if i.get_attribute('required'):
#             i.send_keys("ghbdtn")
#     buton = browser.find_element(By.TAG_NAME,'button')
#     buton.click()
#     time.sleep(1)

#     #находим элемент содержащитй текст
#     welcome_text = browser.find_element(By.TAG_NAME, "h1")
#     #запишем текст из h1 в переменную
#     welcome = welcome_text.text
   
#     #с помощью assert проверяю, что ожидаемый текст совпадает с текстом на странице
#     assert "Congratulations! You have successfully registered!" == welcome
   
# finally:
#     time.sleep(5)
#     browser.quit()

#next lesson
# import math
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By


# link = "https://suninjuly.github.io/get_attribute.html"
# browser = webdriver.Chrome()
# browser.get(link)
# time.sleep(1)


# img_element = browser.find_element(By.ID, 'treasure')


# x_value = img_element.get_attribute('valuex')
# print(x_value)

# import math
# x = int(x_value)
# y = math.log(abs(12 * math.sin(x)))
# print(y)

# input1 = browser.find_element(By.ID, 'answer')
# input1.send_keys(y)

# input2 = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
# input2.click()

# input3 = browser.find_element(By.ID, 'robotsRule')
# input3.click()

# input4 = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
# input4.click()

# time.sleep(5)
# browser.quit()


# # next lesson
# import time

# from selenium import webdriver
# from selenium.webdriver.common.by import By

# from selenium.webdriver.support.ui import Select

# link = "https://suninjuly.github.io/selects1.html"
# browser = webdriver.Chrome()
# browser.get(link)
# time.sleep(1)



# span_element_1 = browser.find_element(By.ID, "num1")
# span_element_2 = browser.find_element(By.ID, "num2")

# text_from_span_1 = span_element_1.text
# text_from_span_2 = span_element_2.text


# number_from_span_1 = int(text_from_span_1)
# number_from_span_2 = int(text_from_span_2)

# print("The numbers are:", number_from_span_1, number_from_span_2)

# sum_of_numbers = number_from_span_1 + number_from_span_2


# print("The sum of the numbers is:", sum_of_numbers)

# # Find the dropdown element
# dropdown = Select(browser.find_element(By.ID, "dropdown"))

# # Select the sum_of_numbers value from the dropdown
# dropdown.select_by_value(str(sum_of_numbers))

# input4 = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
# input4.click()

# time.sleep(5)



# # next lesson
# #Webdriver - это и есть набор команд для управления браузером
# from selenium import webdriver
# #импортируем класс By , который позволяет выбрать способ поиска элемента
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import time

# try:
#     browser = webdriver.Chrome()
#     browser.get("https://suninjuly.github.io/selects1.html")


#     span_element_1 = browser.find_element(By.ID, "num1")
#     text_from_span_1 = span_element_1.text
#     number_from_span_1 = int(text_from_span_1)
#     print(number_from_span_1)
#     span_element_2 = browser.find_element(By.ID, "num2")
#     text_from_span_2 = span_element_2.text
#     number_from_span_2 = int(text_from_span_2)
#     print(number_from_span_2)
#     span_sums = number_from_span_1 + number_from_span_2
#     print(span_sums)
#     select = Select(browser.find_element(By.TAG_NAME, "select"))
#     select.select_by_value(str(span_sums))
#     btn = browser.find_element(By.CSS_SELECTOR,'[type="submit"]')
#     btn.click()
   
# finally:
#     time.sleep(5)
#     browser.quit()


# #next lesson
# import time

# from selenium import webdriver
# from selenium.webdriver.common.by import By

# from selenium.webdriver.support.ui import Select
# import os

# link = "https://suninjuly.github.io/file_input.html"
# browser = webdriver.Chrome()
# browser.get(link)
# time.sleep(1)

# # Find the input fields for first name, last name, and email
# first_name_input = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
# last_name_input = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
# email_input = browser.find_element(By.CSS_SELECTOR, '[name="email"]')

# # Fill out the form with information
# first_name_input.send_keys("John")
# last_name_input.send_keys("Doe")
# email_input.send_keys("johndoe@example.com")

# time.sleep(5)


# # Find the file input element and upload a file
# cur_dir = os.path.abspath(os.path.dirname(__file__))
# file_path = os.path.join(cur_dir, 'file.txt')
# file_input = browser.find_element(By.ID, "file")
# file_input.send_keys(file_path)

# time.sleep(5)


# # Find and click the submit button
# submit_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
# submit_button.click()

# time.sleep(5)

# #Webdriver - это и есть набор команд для управления браузером
# from selenium import webdriver




# #импортируем класс By , который позволяет выбрать способ поиска элемента
# from selenium.webdriver.common.by import By


# from selenium.webdriver.support.ui import Select


# import time


# import os


# try:
#     browser = webdriver.Chrome()
#     browser.get("https://suninjuly.github.io/file_input.html")


#     #Получяем путь к директории текущего исполняемого фйла
#     input_1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
#     input_1.send_keys('asd')
#     input_2 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"')
#     input_2.send_keys('asd')
#     input_3 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
#     input_3.send_keys('asd')






#     cur_dir = os.path.abspath(os.path.dirname(__file__))


#     file_path = os.path.join(cur_dir, 'file.txt')
#     element = browser.find_element(By.CSS_SELECTOR,'[type="file"]')
#     element.send_keys(file_path)


#     btn = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
#     btn.click()

   
# finally:
#     time.sleep(5)
#     browser.quit()


# import os
# import re
# import requests

# # Function to download webpage and its associated CSS files
# def download_webpage_with_css(url, output_dir):
#     # Create output directory if it doesn't exist
#     os.makedirs(output_dir, exist_ok=True)

#     # Send a GET request to fetch the webpage
#     response = requests.get(url)
#     if response.status_code == 200:
#         # Save the HTML content to a file
#         with open(os.path.join(output_dir, 'index.html'), 'w', encoding='utf-8') as f:
#             f.write(response.text)

#         # Find all CSS links in the webpage using regex
#         css_links = re.findall(r'<link.*?rel=["\']stylesheet["\'].*?href=["\'](.*?)["\'].*?>', response.text)
#         for link in css_links:
#             # Construct absolute URLs for CSS files
#             css_url = urljoin(url, link)
#             css_filename = os.path.basename(css_url)
#             # Send a GET request to fetch the CSS file
#             css_response = requests.get(css_url)
#             if css_response.status_code == 200:
#                 # Save the CSS content to a file
#                 with open(os.path.join(output_dir, css_filename), 'w', encoding='utf-8') as f:
#                     f.write(css_response.text)
#             else:
#                 print(f"Failed to download CSS file: {css_url}")
#     else:
#         print(f"Failed to download webpage: {url}")

# # Example usage
# url = "https://suninjuly.github.io/file_input.html"
# output_directory = "downloaded_page"
# download_webpage_with_css(url, output_directory)




# next lesson
#Webdriver - это и есть набор команд для управления браузером
# from selenium import webdriver
# #импортируем класс By , который позволяет выбрать способ поиска элемента
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import time

# try:
#     browser = webdriver.Chrome()
#     browser.get("httpshttps://suninjuly.github.io/alert_accept.html")
#     time.sleep(3)
    
#     alert = browser.switch_to.alert
#     alert.accept()



#     # span_element_1 = browser.find_element(By.ID, "num1")
#     # text_from_span_1 = span_element_1.text
#     # number_from_span_1 = int(text_from_span_1)
#     # print(number_from_span_1)
#     # span_element_2 = browser.find_element(By.ID, "num2")
#     # text_from_span_2 = span_element_2.text
#     # number_from_span_2 = int(text_from_span_2)
#     # print(number_from_span_2)
#     # span_sums = number_from_span_1 + number_from_span_2
#     # print(span_sums)
#     # select = Select(browser.find_element(By.TAG_NAME, "select"))
#     # select.select_by_value(str(span_sums))
#     # btn = browser.find_element(By.CSS_SELECTOR,'[type="submit"]')
#     # btn.click()
   
# finally:
#     time.sleep(5)
#     browser.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Open the webpage
driver = webdriver.Chrome()
driver.get("https://suninjuly.github.io/alert_accept.html")

# Find and click the button to trigger the confirmation
button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
button.click()

# Switch to the alert and accept it
alert = driver.switch_to.alert
alert.accept()

time.sleep(3)

# Find the input field, calculate and input the value
input_field = driver.find_element(By.CSS_SELECTOR, '#answer')
x_value = int(input_field.get_attribute('value'))
input_field.clear()
input_field.send_keys(calc(x_value))

def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

print(calc(x_value))

time.sleep(3)

# Find and click the submit button
submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
submit_button.click()

time.sleep(5)
driver.quit()

# # Solve the captcha on the new page
# # You can add your code here to interact with the elements on the new page and solve the captcha

# # Calculate the result for the new page
# # Find the input field and input the calculated result
# result_input = driver.find_element(By.ID, "answer")
# result_input.send_keys(str(result))

# # Find and submit the form
# submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
# submit_button.click()
# # Wait for a few seconds before closing the browser
# time.sleep(5)
# driver.quit()