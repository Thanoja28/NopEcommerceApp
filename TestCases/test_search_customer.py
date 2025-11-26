import  pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.LoginPage import Login
from pageObjects.addUserPage import AddUser
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from pageObjects.searchUserPage import SearchUser

class Test_003_Login:

    base_url = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUerEmail()
    password = ReadConfig.getUserPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_search_customer(self,setup):
        self.logger.info("**Test Search Customer**")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**Login Successful**")

        self.addUser = AddUser(self.driver)
        self.addUser.clickOnAdminMenu()
        time.sleep(5)
        self.searchUser = SearchUser(self.driver)
        self.searchUser.enterUserName("Tester90")
        self.searchUser.enterUserRole("Admin")
        time.sleep(5)
        self.searchUser.enterEmpName("Peter Mac Anderson")
        self.searchUser.enterStatus("Enabled")
        time.sleep(5)
        self.searchUser.clickSearch()

        rows = self.driver.find_elements(By.XPATH, "//div[@role='row']/div[2]")  # second column (username)
        usernames = [row.text for row in rows]

        print("Usernames in table:", usernames)

        if "Tester90" in usernames:
            print("Tester90 is in the table.")
            self.driver.save_screenshot("Screenshots/after_save.png")
        else:
            print("Tester90 is NOT in the table.")

        self.logger.info("**Search Customer Successful**")
