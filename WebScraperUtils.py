from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class WebScraperUtils:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def obtenir_texte_ou_nan(self, xpath, message_non_specifie="NaN"):
        """Retourne le texte trouvé par le xpath ou un message spécifié s'il n'est pas trouvé."""
        try:
            return self.driver.find_element(By.XPATH, xpath).text
        except NoSuchElementException:
            return message_non_specifie

    def fermer_driver(self):
        """Fermer le navigateur."""
        self.driver.quit()
