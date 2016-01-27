# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import selenium.webdriver.support.ui as ui

class ChartUnshare(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://app.chartcube.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_chart_unshare(self):
        driver = self.driver
        driver.get("https://development.chartcube.com")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("sumedh@codepandora.com")
        driver.find_element_by_id("loginPwd").clear()
        driver.find_element_by_id("loginPwd").send_keys("sam1211212")
        driver.find_element_by_css_selector("button.bottom-right-button.blue-button").click()
        wait = ui.WebDriverWait(driver, 10) # timeout after 10 seconds
        driver.find_element_by_css_selector("div.summary > div.title").click()
        wait = ui.WebDriverWait(driver, 10) # timeout after 10 seconds
        driver.find_element_by_css_selector("div.share_wrap").click()
        wait = ui.WebDriverWait(driver, 10) # timeout after 10 seconds
        driver.find_element_by_id("pillboxAddItem").clear()
        driver.find_element_by_id("pillboxAddItem").send_keys("karuna.lingham@codepandora.com")
        wait = ui.WebDriverWait(driver, 10) # timeout after 10 seconds
        driver.find_element_by_css_selector("#shareOptionsModal > div.modal-container > div.modal-footer > button.bottom-right-button.blue-button").click()
        wait = ui.WebDriverWait(driver, 10) # timeout after 10 seconds
        driver.find_element_by_css_selector("div.share_wrap").click()
        wait = ui.WebDriverWait(driver, 10) # timeout after 10 seconds
        driver.find_element_by_css_selector("a.delete").click()
        wait = ui.WebDriverWait(driver, 10) # timeout after 10 seconds
        driver.find_element_by_css_selector("#shareOptionsModal > div.modal-container > div.modal-footer > button.bottom-right-button.blue-button").click()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()