import pandas as pd
from download import download
from challenge_2021.io import url_db, path_target

class Load_db:
    def __init__(self, url=url_db, target_name=path_target):
        download(url, target_name, replace=False)

    @staticmethod
    def save_as_df():
        totem_raw = pd.read_csv(path_target, na_values="", low_memory=False)
        return totem_raw