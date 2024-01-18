from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait

fake = Faker()

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    print("Launching Browser")


    yield driver
    driver.quit()


def basic_page_authintication(driver):
    #open url
    driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")

    # Verify URL open successfully
    expected_title = "Register Account"
    actual_title = driver.title
    if expected_title == actual_title:
        print(f" open successfully {expected_title}")
    else:
        print(f"open failed Because Actual Result is {actual_title} ")



def test_registration(driver):

    # Registration action

    # find firstname
    username_fname = driver.find_element(By.NAME, "firstname")
    username_fname.send_keys(fake.name())

    # find lastname
    username_lname = driver.find_element(By.NAME, "lastname")
    username_lname.send_keys(fake.name())

    # find email
    username_email = driver.find_element(By.NAME, "email")
    username_email.send_keys(fake.email())
    time.sleep(2)

    # find phone
    username_phone = driver.find_element(By.NAME, "telephone")
    username_phone.send_keys(fake.phone_number())
    time.sleep(2)

    # find password
    username_password = driver.find_element(By.NAME, "password")
    same = fake.password()
    username_password.send_keys(same)
    time.sleep(5)
    print(same)
    # find confirm password
    username_confirm = driver.find_element(By.NAME, "confirm")
    username_confirm.send_keys(same)
    time.sleep(5)

    # find newsletter for yes
    username_newsletter_yes = driver.find_element(By.CSS_SELECTOR,
                                                  "label:nth-of-type(1) > input[name='newsletter']")
    username_newsletter_yes.click()

    # find agree
    username_agree = driver.find_element(By.CSS_SELECTOR, "input[name='agree']")
    username_agree.click()
    time.sleep(3)

    # Submit button
    login_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    # click Submit button
    login_button.click()
    time.sleep(10)

    # verify Registration or not
    expected_url = "https://tutorialsninja.com/demo/index.php?route=account/success"
    actual_url = driver.current_url

    if actual_url == expected_url:
        print(f"Registration successfully.")
    else:
        print(f"Registration Unsuccessful.Test failed.Actual url is {actual_url}")