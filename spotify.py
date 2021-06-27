import os
import pyautogui
from subprocess import run
from selenium import webdriver
import time
import re

# create a file location to store the downloaded file
location = os.path.abspath(os.getcwd()+'\\songs')
#print(location)
os.chdir(location)

link='spotdl '+ pyautogui.prompt(text="link of the song to be downloaded ", title='spotify-downloader')
data=run(link, capture_output=True)
print("downloaded.... ")

name = (data.stdout[33:len(data.stdout)-2]).decode('utf-8')
print(name)

temp_name = re.sub(r"\S*https?:\S*", "", name)
print(temp_name)
if('YouTube' in temp_name):
    original_name= temp_name[118:len(temp_name) - 3]
else:
    original_name =temp_name[29:len(temp_name)-34]           #song name to be printed in case the song is already downloaded
#else:
 #   original_name = temp_name[41:len(temp_name) - 4]

# Till now the file has been downloaded in the pc now to send it to the another person via whatsapp web
receiver_name=input("who do you want to send the song to : ")
options= webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
options.add_argument(r"user-data-dir={x}".format(x=os.getcwd()+'\\'+'user'))
driver=webdriver.Chrome(options=options , executable_path=r'C:\Users\DELL\Downloads\chromedriver_win32\chromedriver.exe')

driver.get("https://web.whatsapp.com/")
time.sleep(10)
user=driver.find_element_by_xpath('//span[@title= "{}"]'.format(receiver_name))
user.click()
time.sleep(2)
attachment=driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]"
                                        "/div[1]/div[2]/div/div/span")
attachment.click()
file=driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[1]/"
                                  "div[2]/div/span/div[1]/div/ul/li[3]/button/span")
file.click()

time.sleep(3)
pyautogui.typewrite(os.getcwd())
pyautogui.press('enter')
time.sleep(2)
pyautogui.typewrite(original_name+".mp3")
pyautogui.press('enter')
print(original_name +".mp3")

time.sleep(2)
send_button=driver.find_element_by_xpath(r"/html/body/div/div[1]/div[1]/div[2]/div[2]/"
                                         r"span/div[1]/span/div[1]/div/div[2]/span/div/div")
send_button.click()













