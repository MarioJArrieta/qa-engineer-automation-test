from selenium.webdriver.common.by import By


class HomeWebElements:
    where_label = (By.XPATH, "//a[@aria-label='Ir a la página principal de kayak']")
    signin_button = (By.XPATH, "//span[contains(text(), 'Iniciar sesión')]")
    search_button = (By.CSS_SELECTOR, "button.RxNS[aria-label='Buscar']")
