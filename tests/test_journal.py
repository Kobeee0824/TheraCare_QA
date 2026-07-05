from pages.login_page import LoginPage
from pages.journal_page import JournalPage

def test_open_journal(driver):

    login = LoginPage(driver)
    journal = JournalPage(driver)

    login.open_page()
    login.login("2023-004", "Test@1234")

    journal.click_journal()

    assert journal.get_journal_heading() == "Journal"

