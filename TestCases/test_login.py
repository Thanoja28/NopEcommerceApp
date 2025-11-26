import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities.readProperties import ReadConfig
from pageObjects.LoginPage import Login
from Utilities.customLogger import LogGen

class Test_001_Login:

    base_url = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUerEmail()
    password = ReadConfig.getUserPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("**Test Home Page Title**")
        self.driver = setup
        self.driver.get(self.base_url)
        act_title = self.driver.title
        if act_title == "OrangeHRM":
            assert True
            print("Actual title is " + act_title)
        else:
            self.driver.save_screenshot("Screenshots/test_login.png")
            assert False

    @pytest.mark.sanity
    def test_login(self, setup):

        self.logger.info("***Test_001_Login***")
        self.logger.info("***Started***")

        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "OrangeHRM":
            assert True
            print("OrangeHRM Login Successful")
            self.logger.info("***OrangeHRM Login Successful***")
        else:
            self.driver.save_screenshot( "Screenshots/test_log.png")
            self.driver.close()
            assert False
    