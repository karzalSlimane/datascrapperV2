import pandas as pd
import time
from constants import *
from WebScraperUtils import WebScraperUtils

class DataScraper:
    def __init__(self, chemin_liens=LINKS_FILE_PATH):
        self.chemin_liens = chemin_liens
        self.utils = WebScraperUtils()
        self.donnees_appartements = []

    def extraire_donnees(self):
        """Extraire les données de chaque lien d'appartement et les stocker dans une liste de dictionnaires."""
        with open(self.chemin_liens, 'r') as f:
            liens = f.readlines()

        for lien in liens:
            self.utils.driver.get(lien.strip())
            time.sleep(2)
            donnee = {
                "titre": self.utils.obtenir_texte_ou_nan(XPATH_TITLE),
                "prix": self.utils.obtenir_texte_ou_nan(XPATH_PRICE),
                "emplacement": self.utils.obtenir_texte_ou_nan(XPATH_LOCATION),
                "type_de_vente": self.utils.obtenir_texte_ou_nan(XPATH_TYPE_DE_VENTE),
                "salon": self.utils.obtenir_texte_ou_nan(XPATH_SALON),
                "chambre": self.utils.obtenir_texte_ou_nan(XPATH_CHAMBRE),
                "toilette": self.utils.obtenir_texte_ou_nan(XPATH_TOILETTE),
                "surface": self.utils.obtenir_texte_ou_nan(XPATH_SURFACE),
                "lien": lien.strip()
            }
            self.donnees_appartements.append(donnee)
        self.utils.fermer_driver()
        return self.donnees_appartements

    def enregistrer_donnees_en_csv(self, chemin=DATA_CSV_PATH):

        """Enregistrer les données des appartements extraites dans un fichier CSV."""
        df = pd.DataFrame(self.donnees_appartements)
        df.to_csv(chemin, index=False)
        print('Données enregistrées dans le fichier CSV.')
