import os
import unittest
from time import sleep
from base_test import BaseTest
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import WebDriverException


class BitbarAndroid(BaseTest):
    def setUp(self):
        super().setUp()
        bitbar_project_name = (
            os.environ.get("BITBAR_PROJECT") or "Android sample project"
        )
        app_package = os.environ.get("BITBAR_APP_PACKAGE") or "com.bitbar.testdroid"
        app_activity = (
            os.environ.get("BITBAR_ACTIVITY") or ".BitbarSampleApplicationActivity"
        )
        if self.bitbar_device == "":
            self._find_device("Android")

        self.capabilities["platformName"] = "Android"
        self.capabilities["bitbar:options"]["project"] = bitbar_project_name
        self.capabilities["bitbar:options"]["device"] = self.bitbar_device
        #self.capabilities["bitbar:options"]["appiumVersion"] = "1.22.3" #launch tests on appium 1
        self.capabilities["appium:automationName"] = "uiautomator2"
        self.capabilities["appium:appPackage"] = app_package
        self.capabilities["appium:appActivity"] = app_activity

    def test_sample(self):
        super()._start_webdriver()
        self.utils.log("  Getting device screen size")
        self.utils.log("  " + str(self.driver.get_window_size()))

        self.utils.screenshot("app_launch")

        self.utils.log("  sleep 300")
        sleep(200)
        self.utils.screenshot("not")
        sleep(40)
        self.utils.screenshot("possible")


def initialize():
    return BitbarAndroid


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(BitbarAndroid)
    unittest.TextTestRunner(verbosity=2).run(suite)
