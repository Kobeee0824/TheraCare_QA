from pages.login_page import LoginPage
from pages.moodtrack_page import MoodTrackPage

def test_moodtrack(driver):
    login = LoginPage(driver)
    moodtrack = MoodTrackPage(driver)
    
    login.open_page()
    login.login("2023-004", "Test@1234")

    moodtrack.click_moodtrack()
    assert moodtrack.get_moodtrack_heading() == "Mood Tracker"


