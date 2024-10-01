from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://2captcha.com/pt/demo/recaptcha-v2")
recaptcha = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "g-recaptcha"))
)
recaptcha.click()

