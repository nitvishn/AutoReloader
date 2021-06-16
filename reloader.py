from selenium import webdriver
from selenium.webdriver.chrome.options import Options
CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
WINDOW_SIZE = "1920,1080"
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                          options=chrome_options
                         )
                        
URL = ""
driver.get("https://vfs-cic.mioot.com/forms/appointments/")
driver.find_element_by_xpath("//select[@id='ddlVac']/option[@value='Bengaluru']").click()
driver.find_element_by_xpath("//select[@id='ddlAlt']/option[@value='0']").click()
driver.find_element_by_xpath("//select[@id='ddlApp']/option[@value='1']").click()
print("Printing elements")
for element in driver.find_elements_by_tag_name("select"):
    print(element.tag_name, element.id)
import time
time.sleep(2)
# driver.close()