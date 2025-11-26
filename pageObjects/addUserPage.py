from selenium.webdriver.common.by import By


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddUser:

    # Menu
    btnAdmin_xpath = "//span[normalize-space()='Admin']"

    # Buttons
    btnAdd_xpath = "//button[normalize-space()='Add']"
    btnSave_xpath = "//button[normalize-space()='Save']"

    # Input fields
    textboxUserRole_xpath = "//label[text()='User Role']/following::div[contains(@class,'oxd-select-text')]"
    optionUserRoleAdmin_xpath = "//div[@role='listbox']//span[text()='Admin']"

    textboxEmpName_xpath = "//input[@placeholder='Type for hints...']"

    textboxStatus_xpath = "//label[text()='Status']/following::div[contains(@class,'oxd-select-text')]"
    optionStatusEnabled_xpath = "//div[@role='listbox']//span[text()='Enabled']"

    textboxUsername_xpath = "//label[text()='Username']/following::input"
    textboxPassword_xpath = "//label[text()='Password']/following::input"
    textboxConfirmPassword_xpath = "//label[text()='Confirm Password']/following::input"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Click Admin menu
    def clickOnAdminMenu(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btnAdmin_xpath))).click()

    # Click Add button
    def clickOnAdd(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btnAdd_xpath))).click()

    # User Role dropdown
    def selectUserRole(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.textboxUserRole_xpath))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.optionUserRoleAdmin_xpath))).click()

    # Employee Name
    def enterEmpName(self, name):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.textboxEmpName_xpath))).send_keys(name)

    # Status dropdown
    def selectStatus(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.textboxStatus_xpath))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.optionStatusEnabled_xpath))).click()

    # Username
    def enterUsername(self, username):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.textboxUsername_xpath))).send_keys(username)

    # Password
    def enterPassword(self, password):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.textboxPassword_xpath))).send_keys(password)

    # Confirm Password
    def enterConfirmPassword(self, password):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.textboxConfirmPassword_xpath))).send_keys(password)

    # Save
    def clickOnSave(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btnSave_xpath))).click()






