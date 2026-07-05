from pages.login_page import LoginPage
from pages.appointment_page import AppointmentPage

def test_appointment(driver):
    login = LoginPage(driver)
    appointment = AppointmentPage(driver)

    login.open_page()
    login.login("2023-004", "Test@1234")

    appointment.click_appointment()
    assert appointment.get_appointment_title() == "Appointments"

