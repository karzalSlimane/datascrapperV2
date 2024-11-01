# constants.py

# URL de base pour le scraping
BASE_URL = "https://www.avito.ma/fr/maroc/"

# Temps d'attente pour le chargement des pages (en secondes)
WAIT_TIME = 2

# Chemins des fichiers
LINKS_FILE_PATH = "href.txt"
DATA_CSV_PATH = "appartements_data.csv"

# Sélecteurs XPATH
XPATH_TITLE = "//div[@class='sc-1g3sn3w-9 kvOteU']"
XPATH_PRICE = "//p[@class='sc-1x0vz2r-0 lnEFFR sc-1g3sn3w-13 czygWQ']"
XPATH_LOCATION = "//span[@class='sc-1x0vz2r-0 iotEHk']"
XPATH_TYPE_DE_VENTE = "//li[@class='sc-qmn92k-1 jJjeGO']/span[@class='sc-1x0vz2r-0 gSLYtF' and contains(text(),'Appartements, à vendre')]"
XPATH_SALON = "//li[.//span[text()='Salons']]/span[@class='sc-1x0vz2r-0 gSLYtF']"
XPATH_CHAMBRE = "//*[@id='__next']/div/main/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div/span"
XPATH_TOILETTE = "//*[@id='__next']/div/main/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[4]/div[1]/div[2]/div/span"
XPATH_SURFACE = "//li[.//span[text()='Surface habitable']]/span[@class='sc-1x0vz2r-0 gSLYtF']"
