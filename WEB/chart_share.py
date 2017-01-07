#! /usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import time
import re


class ChartShare(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_chart_share(self):
        driver = self.driver
        print "Selenium Test Case: cp Web: Share"
        driver.get("http://development.cp.com/")
        time.sleep(15)

        driver.find_element_by_css_selector(
            "input[name=\"email\"]").send_keys("sumedh@codepandora.com")
        time.sleep(5)

        driver.find_element_by_id("loginPwd").send_keys("sam1211212")
        time.sleep(5)

        driver.find_element_by_css_selector(
            "button.bottom-right-button.blue-button").click()
        time.sleep(35)

        driver.find_element_by_xpath(
            "//div[2]/div[3]/div/div/div[2]/div[2]/div").click()
        time.sleep(5)

        driver.find_element_by_xpath(
            "//div[@id='cubeView']/div[2]/div[2]/div[3]/div").click()
        time.sleep(5)

        driver.find_element_by_id("pillboxAddItem").send_keys(
            "karuna.lingham@codepandora.com")
        time.sleep(5)

        driver.find_element_by_css_selector(
            "textarea.note-field").send_keys("Web Share").clear()
        driver.find_element_by_css_selector(
            "textarea.note-field").send_keys("Web Share")
        time.sleep(5)

        driver.find_element_by_css_selector(
            "#shareOptionsModal > div.modal-container > div.modal-footer > button.bottom-right-button.blue-button").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
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
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
