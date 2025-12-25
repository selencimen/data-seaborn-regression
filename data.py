from pathlib import Path
import pandas as pd


class Olist:
    def get_data(self):
        csv_path = Path("~/workintech/olist/data/csv").expanduser()

        file_paths = list(csv_path.iterdir())
        file_names = [p.name for p in file_paths]

        key_names = [
            name.replace("olist_", "")
                .replace("_dataset", "")
                .replace(".csv", "")
            for name in file_names
        ]

        data = {}
        for key, path in zip(key_names, file_paths):
            data[key] = pd.read_csv(path)

        return data
