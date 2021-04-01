import os


url_db_bera = "https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H19070220_archive.json"
path_target_txt_bera = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../data_vis", "data_txt", "beracasa.txt")
path_target_json_bera = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../data_vis", "data_json", "beracasa.json")
path_target = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data_json", "beracasa.json")