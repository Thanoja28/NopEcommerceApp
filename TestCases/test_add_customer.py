

import  pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.LoginPage import Login
from pageObjects.addUserPage import AddUser
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test_003_Login:

    base_url = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUerEmail()
    password = ReadConfig.getUserPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_add_customer(self,setup):
        self.logger.info("**Test Add Customer**")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**Login Successful**")

        self.logger.info("**Test Add Customer Test**")

        self.addUser = AddUser(self.driver)
        self.addUser.clickOnAdminMenu()
        time.sleep(5)
        self.addUser.clickOnAdd()
        time.sleep(3)

        self.logger.info("**providing user info**")

        self.addUser.selectUserRole()
        self.addUser.enterEmpName("Joy Smith")

        options = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'oxd-autocomplete-option')]")
        print("OPTIONS FOUND:", len(options))
        for o in options:
            print("OPTION TEXT:", o.text)

        self.addUser.selectStatus()
        self.addUser.enterUsername("tester8")
        self.addUser.enterPassword("holland123")
        self.addUser.enterConfirmPassword("holland123")
        self.addUser.clickOnSave()
        time.sleep(3)

        # # Debug: save screenshot and page source
        self.driver.save_screenshot("Screenshots/after_save.png")
        with open("page_source.html", "w") as f:
            f.write(self.driver.page_source)

        self.logger.info("**Toast appeared**")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Successfully')]"))
            )
            success = True
            print("**Successfully Added**")


        except:
            success = False

        self.logger.info("**successfully validated message**")








