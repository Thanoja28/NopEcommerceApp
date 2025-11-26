
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Login:
    textbox_username_xpath = "//input[@name='username']"
    textbox_password_xpath = "//input[@name='password']"
    button_login_xpath = "//button[@type='submit']"
    user_dropdown_xpath = "//span[@class='oxd-userdropdown-tab']"
    logout_link_xpath = "//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # -------------------------
    # Wait for login page
    # -------------------------
    def waitForLoginPage(self):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.textbox_username_xpath))
        )

    # -------------------------
    # Login actions
    # -------------------------
    def setUserName(self, username):
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.textbox_username_xpath))
        )
        element.clear()
        element.send_keys(username)

    def setPassword(self, password):
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.textbox_password_xpath))
        )
        element.clear()
        element.send_keys(password)

    def clickLogin(self):
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.button_login_xpath))
        ).click()

    # -------------------------
    # Logout actions
    # -------------------------
    def clickLogout(self):
        try:
            # Click user dropdown (top-right corner)
            dropdown = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, self.user_dropdown_xpath))
            )
            dropdown.click()

            # Click the logout link
            logout = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, self.logout_link_xpath))
            )
            logout.click()

            # After logout, wait until login page appears
            self.waitForLoginPage()

        except Exception as e:
            print("Logout failed — likely because login attempt was invalid.")





