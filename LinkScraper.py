from selenium.webdriver.common.by import By
import time
from constants import BASE_URL, WAIT_TIME, LINKS_FILE_PATH
from WebScraperUtils import WebScraperUtils

class LinkScraper:
    def __init__(self, produit, nombre_pages=2):
        self.produit = produit
        self.nombre_pages = nombre_pages
        self.liens = []
        self.utils = WebScraperUtils()

    def extraire_liens(self):
        """Extraire les liens d'appartements sur plusieurs pages."""
        url_de_base = f"{BASE_URL}{self.produit}"

        for page in range(1, self.nombre_pages + 1):
            url = url_de_base if page == 1 else f"{url_de_base}?o={page}"
            self.utils.driver.get(url)

            time.sleep(WAIT_TIME)

            elements_appartements = self.utils.driver.find_elements(By.XPATH, "//a[@class='sc-1jge648-0 eTbzNs']")
            for element in elements_appartements:
                lien = element.get_attribute('href')
                if lien:
                    self.liens.append(lien)

        self.utils.fermer_driver()
        return self.liens

    def enregistrer_liens_dans_fichier(self, chemin=LINKS_FILE_PATH):
        """Enregistrer les liens extraits dans un fichier."""
        with open(chemin, 'w', encoding='utf-8') as fichier:
            for lien in self.liens:
                fichier.write(lien + '\n')
        print('Liens enregistrés dans le fichier.')
