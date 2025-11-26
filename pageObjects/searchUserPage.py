import time

from selenium.webdriver.common.by import By


class SearchUser:
    txtBoxUsername_xpath = "//input[contains(@class, 'oxd-input') and contains(@class, 'oxd-input--active')]"
    textUserRole_xpath = "//label[text()='User Role']/parent::div/following-sibling::div//div[@class='oxd-select-text-input']"
    drpAdmin_xpath = "//div[@class='oxd-select-text-input' and text()='Admin']"
    texEmpName_xpath = "//input[contains(@placeholder, 'Type for hints')]"
    txtStatus_xpath = "//div[@class='oxd-select-text-input' and text()='-- Select --']"
    drpStatus_xpath = "//div[@class='oxd-select-text-input' and text()='Enabled']"
    btnSearch_xpath = "//button[normalize-space()='Search']"


    # Table locators
    fullTable_xpath = "//div[contains(@class, 'orangehrm-container')]"
    innerTable_xpath = "//div[@class= 'oxd-table']"



    def __init__(self, driver):
        self.driver = driver

    def enterUserName(self, name):
        self.driver.find_element(By.XPATH, self.txtBoxUsername_xpath).send_keys(name)
    # def enterUserRole(self, name):
    #     self.driver.find_element(By.XPATH, self.textUserRole_xpath).send_keys(name)
    #     self.driver.find_element(By.XPATH, self.drpAdmin_xpath).click()
    def enterEmpName(self, name):
        self.driver.find_element(By.XPATH, self.texEmpName_xpath).send_keys(name)
    # def enterStatus(self, name):
    #     self.driver.find_element(By.XPATH, self.drpStatus_xpath).send_keys(name)
    #     self.driver.find_element(By.XPATH, self.drpStatus_xpath).click()
    def clickSearch(self):
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()

    def enterUserRole(self, role_name):
        # Click to open the User Role dropdown
        dropdown_xpath = "//label[text()='User Role']/../following-sibling::div//div[contains(@class,'oxd-select-text-input')]"
        self.driver.find_element(By.XPATH, dropdown_xpath).click()
        time.sleep(1)  # wait for dropdown options to show

        # Click the role option
        option_xpath = f"//div[@role='option']//span[text()='{role_name}']"
        self.driver.find_element(By.XPATH, option_xpath).click()

    def enterStatus(self, status_name):
        # Click to open the Status dropdown
        dropdown_xpath = "//label[text()='Status']/../following-sibling::div//div[contains(@class,'oxd-select-text-input')]"
        self.driver.find_element(By.XPATH, dropdown_xpath).click()
        time.sleep(1)  # wait for dropdown options to show

        # Click the status option
        option_xpath = f"//div[@role='option']//span[text()='{status_name}']"
        self.driver.find_element(By.XPATH, option_xpath).click()





