import glob
import pandas as pd


# Fonction pour charger tous les fichiers CSV dans un dossier spécifique
def load_data(folder_path):
    # Liste de tous les fichiers CSV dans le dossier
    csv_files = glob.glob(folder_path + "/*.csv")

    # Charger chaque fichier CSV et les concaténer
    all_data = pd.DataFrame()
    for file in csv_files:
        data = pd.read_csv(file)
        all_data = pd.concat([all_data, data])

    return all_data


# Chemin du dossier contenant les fichiers CSV
folder_path = "Data_cleanig_simple_test\real_test_case"

# Charger les données
data = load_data(folder_path)
