from selenium.webdriver.common.by import By


class HomeWebElements:
    where_label = (By.CSS_SELECTOR, '[aria-label="Ir a la página principal de kayak"]')
    signin_button = (By.CSS_SELECTOR, '.common-layout-react-HeaderAccountWrapper span div[role="button"]')
    search_button = (By.CSS_SELECTOR, 'button[aria-label="Buscar"]')
    tile_label = (By.XPATH, "//span[contains(.,'Compara ofertas de vuelos en cientos de webs')]")
    main_functions_menu = (By.CSS_SELECTOR, "ul[role='menubar']")
    search_destiny_input = (By.CSS_SELECTOR, 'input[aria-label="Destino"]')
    general_menu_button = (By.CSS_SELECTOR, 'div[aria-label="Abrir navegación principal"]')
