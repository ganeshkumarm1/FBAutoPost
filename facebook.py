import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
browser = webdriver.Chrome()
browser.get("http://www.facebook.com")
email = browser.find_element_by_name("email")
email.send_keys("your_user_name",Keys.TAB)
pw = browser.find_element_by_name("pass")
pw.send_keys("Your_password",Keys.RETURN)
time.sleep(60)
print "Started"
post_msg=browser.find_element_by_css_selector(".uiTextareaAutogrow")
post_msg.send_keys("your_message")
ActionChains(browser).key_down(Keys.CONTROL).send_keys(Keys.RETURN).perform();
