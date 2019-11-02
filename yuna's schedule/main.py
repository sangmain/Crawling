from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.maximize_window()

user_id = ""
user_pw = ""
with open("yuna's schedule/id.txt", 'r') as f:
    user_id = f.readline()
with open("yuna's schedule/pw.txt", 'r') as f:
    user_pw = f.readline()

driver.get('https://cas.ut-capitole.fr/cas/login?service=http://monespace.ut-capitole.fr/Login')

userid_element = driver.find_element_by_id('username')
userid_element.send_keys(user_id)

userpw_element = driver.find_element_by_id('password')
userpw_element.send_keys(user_pw)

login_btn = driver.find_element_by_id('connexion')
login_btn.click()

driver.get('http://monespace.ut-capitole.fr/tag.4fffb8452a630002.render.userLayoutRootNode.uP?uP_root=u105l1n3292&uP_sparam=activeTab&activeTab=4')

sleep(20)
driver.save_screenshot("yuna's schedule/screenshot.png")
print('저장완료')


# driver.get('http://sangmin99554.pythonanywhere.com/upload/')

driver.quit()