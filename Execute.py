from DataScraper import DataScraper
from LinkScraper import LinkScraper

# Initialiser le scraper de liens pour les appartements
scraper_liens = LinkScraper(produit="appartement")
liens = scraper_liens.extraire_liens()
scraper_liens.enregistrer_liens_dans_fichier("href.txt")

# Initialiser le scraper de données avec les liens extraits
scraper_donnees = DataScraper("href.txt")
donnees_appartements = scraper_donnees.extraire_donnees()
scraper_donnees.enregistrer_donnees_en_csv("appartements_data.csv")
