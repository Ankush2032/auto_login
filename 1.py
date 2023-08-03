import  time
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
fake_data = Faker()
class DemoFindElementByXPATH():

    def locate_element_By_XPATH(self):
        driver = webdriver.Chrome()
        driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH,"//input[@id='login-input']").send_keys('test@test.uo')
        driver.find_element(By.XPATH,"(//button[@id='login-continue-btn'])[1]").click()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, '//*[@id="signup-mobile-number"]').send_keys(fake_data.phone_number())
        driver.find_element(By.XPATH,'//*[@id="signup-password"]').send_keys(fake_data.password())
        driver.implicitly_wait(5)
        # driver.find_element(By.XPATH,'//*[@id="login-submit-btn"]').click()
        time.sleep(100)
findbyxpath = DemoFindElementByXPATH()
findbyxpath.locate_element_By_XPATH()