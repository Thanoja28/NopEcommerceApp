
import time
import pytest
from selenium.webdriver.common.by import By

from Utilities.readProperties import ReadConfig
from pageObjects.LoginPage import Login
from Utilities.customLogger import LogGen
from Utilities.excelUtils import ExcelUtils


class Test_002_DDT_Login:

    base_url = ReadConfig.getApplicationUrl()
    path = "TestData/testData.xlsx"

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_DDT(self, setup):

        self.logger.info("********** Test_002_DDT_Login STARTED **********")

        self.driver = setup
        self.driver.get(self.base_url)

        self.lp = Login(self.driver)
        self.lp.waitForLoginPage()

        self.rows = ExcelUtils.getRowCount(self.path, "Sheet1")
        self.logger.info(f"Total Rows in Excel: {self.rows}")

        lst_status = []  # to track test case results

        # LOOP THROUGH EXCEL ROWS
        for row in range(2, self.rows + 1):

            user = ExcelUtils.readData(self.path, "Sheet1", row, 2) or ""
            pwd = ExcelUtils.readData(self.path, "Sheet1", row, 3) or ""
            exp = ExcelUtils.readData(self.path, "Sheet1", row, 4) or ""

            self.logger.info(f"Row {row - 1} → USER: {user}, EXP: {exp}")

            # ALWAYS GO TO LOGIN PAGE BEFORE ATTEMPT
            self.driver.get(self.base_url)
            self.lp.waitForLoginPage()

            # Perform login
            self.lp.setUserName(user)
            self.lp.setPassword(pwd)
            self.lp.clickLogin()
            time.sleep(2)

            try:
                self.driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']")
                login_success = True
            except:
                login_success = False

            # Expected Output
            if login_success:
                if exp == "pass":
                    self.logger.info("Login Successful → PASS")
                    lst_status.append("PASS")
                    self.lp.clickLogout()
                else:
                    self.logger.info("Login Unexpectedly Successful → FAIL")
                    lst_status.append("FAIL")
                    self.lp.clickLogout()

            else:
                if exp == "fail":
                    self.logger.info("Login Failed as Expected → PASS")
                    lst_status.append("PASS")
                else:
                    self.logger.info("Login Failed Unexpectedly → FAIL")
                    lst_status.append("FAIL")




