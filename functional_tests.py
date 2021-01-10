from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self): 
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Jack check out a new todo list website
        self.browser.get('http://localhost:8000')

        # He sees that the page header mentions todo
        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)  
        self.fail('Finish the test!')  

        # He is invited to enter a  to-do item straight away

        # He writes "Do the laundry" into a text box

        # When he hits enter, the page refreshes and now the page lists "1. Do the Laundry"

        # There is still a text box inviting him to enter another todo, he enters "Lolz"

        # The page updates again, and now shows both item on the list

        # Jack wonder if the site will remember his list, then he sees the site generated a unique link for him

        # He visits that URL, the todo list is still there

        # Satisfied, he goes back to sleep

if __name__ == '__main__':
    unittest.main()
