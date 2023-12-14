from selenium import webdriver
from selenium.webdriver.common.by import By
import time
EMAIL = "your.email77@gmail.com"
PASS = "password to linkedin"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3720000533&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")
driver.maximize_window()

popup_dismiss = driver.find_element(By.XPATH, value='/html/body/div[6]/a[1]')
time.sleep(2)
popup_dismiss.click()
time.sleep(2)
accept_cookie = driver.find_element(By.XPATH, value='//*[@id="artdeco-global-alert-container"]/div/section/div/div[2]/button[1]')
accept_cookie.click()
time.sleep(2)
email = driver.find_element(By.CSS_SELECTOR, value='input[id="username"]')
email.send_keys(EMAIL)
password = driver.find_element(By.CSS_SELECTOR, value='input[id="password"]')
password.send_keys(PASS)
sign_button = driver.find_element(By.CSS_SELECTOR, value='button[type="submit"')
sign_button.click()
time.sleep(2)
change_experience_button = driver.find_element(By.CSS_SELECTOR, value='button[id="searchFilter_experience"')
change_experience_button.click()
intership = driver.find_element(By.XPATH, value='//*[@id="artdeco-hoverable-artdeco-gen-43"]/div[1]/div/form/fieldset/div[1]/ul/li[2]/label/p/span[1]')
intership.click()
see_results = driver.find_element(By.XPATH, value='//*[@id="artdeco-hoverable-artdeco-gen-43"]/div[1]/div/form/fieldset/div[2]/button[2]/span')
see_results.click()
time.sleep(5)
easy_apply = driver.find_element(By.CSS_SELECTOR, value=".jobs-s-apply button")
easy_apply.click()




