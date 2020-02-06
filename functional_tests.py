from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Erin has heard about a cool new online to-do app. She goes to check out its homepage:
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        assert 'To-Do' in self.browser.title, "Browser title was " + self.browser.title

        # She is invited to enter a to-do item straight away

        # She types "Buy Mary Kay items" into a text box (Erin's business is selling cosmetics)

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy Mary Kay items" as an item in the to-do lists

        # There is still a text box inviting her to add another item. She enters "Schedule party"

        # The page updates again, and now shows both items on her list

        # Erin wonders whether the site will remember her list. Then she sees that the site has generated a unique URL for her
        # (There is some explanatory text to that effect)

        # She visits that URL = her to-do list is still there!

        # Satisfied and organized, she goes back to sleep.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
