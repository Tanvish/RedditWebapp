from django.test import TestCase
import praw
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest
import time

from . import views
# Create your tests here.

import re

class SubredditTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("/Users/tanvishjha/Downloads/chromedriver")

    def test_home_page(self):
        self.driver.get("http://127.0.0.1:8000/")
        src = self.driver.page_source
        text_found = re.search(r'Welcome to my subreddit simulation. Please enter a subreddit that you can think of to proceed.', src)
        self.assertNotEqual(text_found, None)

    def test_basic_case(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.find_element_by_id('input-form').send_keys("python")
        self.driver.find_element_by_id('search').click()
        self.assertIn("http://127.0.0.1:8000/", self.driver.current_url)

    def test_now_showing(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.find_element_by_id('input-form').send_keys("python")
        self.driver.find_element_by_id('search').click()
        src = self.driver.page_source
        text_found = re.search(r'Now showing: python', src)
        self.assertNotEqual(text_found, None)

    def test_now_showing_does_not_show(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.find_element_by_id('input-form').send_keys("pytho")
        self.driver.find_element_by_id('search').click()
        src = self.driver.page_source
        text_found = re.search(r'Now showing:', src)
        self.assertEqual(text_found, None)

    def test_shows_error_message_for_invalid_subreddit(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.find_element_by_id('input-form').send_keys("pytho")
        self.driver.find_element_by_id('search').click()
        src = self.driver.page_source
        text_found = re.search(r'Please enter a valid subreddit in the search bar above.', src)
        self.assertNotEqual(text_found, None)


    def tearDown(self):
        self.driver.quit

    if __name__ == '__main__':
        unittest.main()