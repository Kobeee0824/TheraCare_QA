from pages.login_page import LoginPage
from pages.learning_materials import LearningMaterials

def test_learning_materials(driver):
    login = LoginPage(driver)
    learning_materials = LearningMaterials(driver)

    login.open_page()

    login.login("2023-004", "Test@1234")

    learning_materials.click_learning_materials()
    assert learning_materials.get_learning_materials_title() == "Learning Materials"

