from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  # Add this line to import the 'time' module

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

try:
    # Navigate to the login page
    driver.get("D:/project/public/login.html")

    # Find the email and password input fields
    email_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "password")

    # Enter the email and password
    email_field.send_keys("vsrmule@gmail.com")
    time.sleep(2)

    password_field.send_keys("2704")
    time.sleep(2)

    # Submit the form
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    # Wait for the alert to appear
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())

    # Accept the alert
    alert.accept()
    time.sleep(2)

    # Navigate to the weather page
    driver.get("D:/project/public/weatherindex.html")

    # Find the location input and submit button
    input_field = driver.find_element(By.ID, "location-input")
    submit_button = driver.find_element(By.ID, "fetchButton")

    # Enter the city in the location input
    input_field.send_keys("New York")
    time.sleep(2)
    # Click the submit button
    submit_button.click()

    # Wait for 5 seconds for the weather details to load
    driver.implicitly_wait(5)

    # Find the feedback input and submit feedback button
    feedback_input = driver.find_element(By.ID, "feedback-input")
    feedback_button = driver.find_element(By.ID, "submitFeedbackButton")

    # Enter the feedback in the input
    feedback = "The weather information is accurate and helpful."
    feedback_input.send_keys(feedback)

    # Click the submit feedback button
    feedback_button.click()

    # Wait for a moment to ensure the feedback submission is complete
    time.sleep(2)

finally:
    # Close the browser
    driver.quit()
