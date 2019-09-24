from selenium import webdriver
from time import sleep
import mms as mms
import requests
import threading
import time

from bs4 import BeautifulSoup

# 드로우 목록 불러오기
def load_draw_list():

    # driver = webdriver.PhantomJS()
    driver = webdriver.Firefox()
    driver.minimize_window()


    driver.get('https://www.nike.com/launch/')

    # html = driver.page_sourceq

    # print(html)
    sl_items = driver.find_elements_by_xpath("//div[@data-qa='shop-now-cta']")

    shoe_avail = []
    for x in sl_items:
        itemHTML = x.get_attribute('innerHTML')
        if 'Buy' in itemHTML:
            href = itemHTML[231:]
            shoe_avail.append(href[:-12])
            # print(itemHTML)
            # print(len(itemHTML))
            # print(href)

    driver.quit()
    return shoe_avail



# 이미 불러온 데이터와 현재 데이터와 비교해 바뀐점을 찾기
def cmp_old_new(new_shoelist, old_shoelist):
    print("new shoelist", new_shoelist)

    updated_shoe = []
    for x in new_shoelist:
        if not x in old_shoelist:
            print("shoes updated")
            updated_shoe.append(x)

    old_shoelist = new_shoelist.copy()

    return updated_shoe, old_shoelist



#바뀐점을 이메일로 보낸다
def send_MMS(updated_shoe, old_shoelist):
    
    to_update = shoe_list = ""

    for x in updated_shoe:
        x = x.replace("-", " ")
        to_update = to_update + x + "\n"
    for x in old_shoelist:
        x = x.replace("-", " ")
        shoe_list = shoe_list + x + "\n"

    message = "새로운 항목\n" + to_update + "\n판매중\n" + shoe_list


    mms.sendMail('sangmin010203@gmail.com', 'sangmin010203@gmail.com', message)
    # mms.sendMail('sangmin010203@gmail.com', 'vinny9808@gmail.com', message)
    # mms.sendMail('sangmin010203@gmail.com', 'vogherahyun@gmail.com', message)
    

#스레드 함수와 함깨 계속 실행될 코드
thread_time = 1800
old_shoelist = []

def main():
    global old_shoelist
    updated_shoe, old_shoelist = cmp_old_new(load_draw_list(), old_shoelist)
    if updated_shoe:
        print("updated")
        print(updated_shoe)

        with open("Nike/shoe_list.txt", 'w') as f:
            for x in old_shoelist:
                f.write(x)
        
        send_MMS(updated_shoe, old_shoelist)

    else:
        print("nothing to update")


    print("1 thread end \n\n")
    threading.Timer(thread_time, main).start()


with open("Nike/shoe_list.txt", 'r') as f:
    old_shoelist = f.readline()

print("import Shoe: ", old_shoelist)
main()