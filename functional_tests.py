from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Jack check out a new todo list website
        self.browser.get("http://localhost:8000")

        # He sees that the page header mentions todo
        # She notices the page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("To-Do", header_text)

        # He is invited to enter a  to-do item straight away
        inputbox = self.browser.find_element_by_id("id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a to-do item")

        # He writes "Do the laundry" into a text box
        inputbox.send_keys("Do the laundry")

        # When he hits enter, the page refreshes and now the page lists
        # "1. Do the Laundry"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table("1. Do the laundry")

        # There is still a text box inviting her to add another item. He
        # enters "Lolz"
        inputbox = self.browser.find_element_by_id("id_new_item")
        inputbox.send_keys("Lolz")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table("1. Do the laundry")
        self.check_for_row_in_list_table("2. Lolz")

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.
        self.fail("Finish the test!")

    # He visits that URL, the todo list is still there

    # Satisfied, he goes back to sleep


if __name__ == "__main__":
    unittest.main()
