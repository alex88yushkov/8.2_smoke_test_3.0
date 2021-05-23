from selenium import webdriver
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.by import By # Alexander Yushkov -- 05/22/21
from selenium.webdriver.support.ui import WebDriverWait # Alexander Yushkov -- 05/22/21
from selenium.webdriver.support import expected_conditions as EC # Alexander Yushkov -- 05/22/21
from selenium.webdriver.support.select import Select # Alexander Yushkov -- 05/22/21

driver = webdriver.Chrome(executable_path='drivers/chromedriver')
driver.get("https://techskillacademy.net/brainbucket/index.php?route=account/login")

driver.maximize_window()

wd_wait = WebDriverWait(driver, 10) # Alexander Yushkov -- 05/22/21
click = EC.element_to_be_clickable # Alexander Yushkov -- 05/22/21

# LOGIN PAGE
logo = driver.find_element_by_xpath("//img[@title='Brainbucket']")

# Alexander Yushkov -- 05/09/21
password_field = driver.find_element_by_id("input-password")
password_field.clear()
password_field.send_keys("123qwe123qweasdzc")

# Alexander Yushkov -- 05/09/21
# login_btn = driver.find_element_by_xpath("//input[@value='Login']")
login_btn = wd_wait.until(click((By.XPATH, "//input[@value='Login']"))) # Alexander Yushkov -- 05/22/21

# Alexander Yushkov -- 05/09/21 (Optional)
background_color = login_btn.value_of_css_property("background-color")
converted_background_color = Color.from_string(background_color)
assert converted_background_color.rgb == 'rgb(34, 154, 200)'

# Alexander Yushkov -- 05/09/21
login_btn.click()

# Alexander Yushkov -- 05/09/21
new_registrant_btn = driver.find_element_by_xpath("//a[contains(text(), 'Continue')]")

# getting the background color of the button
background_color = new_registrant_btn.value_of_css_property("background-color")
# converted_background_color = Color.from_string(background_color)
assert converted_background_color.rgb == 'rgb(34, 154, 200)'
new_registrant_btn.click()

# Register Account PAGE

wd_wait.until(EC.title_is("Register Account")) # Alexander Yushkov -- 05/22/21

# Alexander Yushkov -- 05/09/21
fields = [("2", "firstname", "Alexander"), ("3", "lastname", "Yushkov"),
          ("4", "email", "test@test.com"), ("5", "telephone", "123-123-1231")]
# Alexander Yushkov -- 05/09/21
for field in fields:
    some_field = driver.find_element_by_xpath("//fieldset/div[%s]" % field[0])
    field_input = driver.find_element_by_id('input-%s' % field[1])
    field_class = some_field.get_attribute("class")
    assert "required" in field_class
    field_input.clear()
    field_input.send_keys("%s" % field[2])

# Alexander Yushkov -- 05/09/21
fax_field = driver.find_element_by_xpath("//fieldset/div[6]")
fax_input = driver.find_element_by_id('input-fax')
fax_field_class = fax_field.get_attribute("class")
assert "required" not in fax_field_class

# Alexander Yushkov -- 05/09/21
fax_input.clear()
fax_input.send_keys("321-543-9877")

################### Exercise #1
# Alexander Yushkov -- 05/22/21:
state_dropdown = driver.find_element_by_id("input-zone")
state_dropdown_select = Select(state_dropdown)
state_dropdown_select.select_by_value("3635") # Illinois

policy_box = driver.find_element_by_xpath("//input[@name='agree' and @value='1']")
if not policy_box.is_selected():
    policy_box.click()

subscribe_btn = driver.find_element_by_xpath("//input[@name='newsletter' and @value='0']")
if not subscribe_btn.is_selected():
    subscribe_btn.click()
################### /Exercise #1

################### Exercise #2:
# Alexander Yushkov -- 05/22/21
account_btn = driver.find_element_by_xpath("//a[@title='My Account']")
account_btn.click()

wd_wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']")))

register_option = driver.find_element_by_xpath("//a[contains(text(),'Register')]")
register_option.click()

reg_page_header = wd_wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='content']/h1")))
assert reg_page_header.text == "Register Account"

account_btn = driver.find_element_by_xpath("//a[@title='My Account']")
account_btn.click()
wd_wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']")))

register_option = driver.find_element_by_xpath("//a[contains(text(),'Login')]")
register_option.click()

wd_wait.until(EC.title_is("Account Login"))
################### /Exercise #2


driver.close()