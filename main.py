import pandas as pd
import os


def clean_data(data):
    data.drop_duplicates(inplace=True)

    data.dropna(inplace=True)

    data["count"] = data["count"].astype(int)

    data.reset_index(drop=True, inplace=True)

    return data


folder_path = "."

output_folder = "real_test_case_done"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

csv_files = [file for file in os.listdir(folder_path) if file.endswith(".csv")]

for csv_file_name in csv_files:
    data = pd.read_csv(os.path.join(folder_path, csv_file_name))

    cleaned_data = clean_data(data)

    cleaned_file_name = os.path.join(output_folder, csv_file_name)

    cleaned_data.to_csv(cleaned_file_name, index=False)

    print(f"Données nettoyées enregistrées dans '{cleaned_file_name}'.")

print("Nettoyage des fichiers CSV terminé.")
