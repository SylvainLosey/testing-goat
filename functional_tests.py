from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

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

        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertTrue(
            any(row.text == "1. Do the laundry" for row in rows),
            "New to-do item did not appear in table",
        )

        # There is still a text box inviting him to enter another todo, he enters "Lolz"
        self.fail("Finish the test!")

        # The page updates again, and now shows both item on the list

        # Jack wonder if the site will remember his list, then he sees the site
        # generated a unique link for him

        # He visits that URL, the todo list is still there

        # Satisfied, he goes back to sleep


if __name__ == "__main__":
    unittest.main()
