# autonomousAJ_googleCalendarAPI/autonomousAJ_googleCalendarAPI/data/colors_data.py
# Endpoint: colors
# URL: {'proper_name': 'Colors', 'url': nan}
import pandas as pd
from autonomousAJ_googleCalendarAPI.api.colors import Colors
from autonomousAJ_googleCalendarAPI.config import global_config

class Colors_Data:
    def __init__(self):
        self.colors = Colors()

    def get_and_process_data(self):
        data = self.colors.get_colors()
        df = pd.DataFrame(data)
        return df

    def save_data(self, df):
        # df.to_csv(FILE_PATH, index=False)
        print(df)
