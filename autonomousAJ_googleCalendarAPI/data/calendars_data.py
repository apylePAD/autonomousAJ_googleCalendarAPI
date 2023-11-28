# autonomousAJ_googleCalendarAPI/autonomousAJ_googleCalendarAPI/data/calendars_data.py
# Endpoint: calendars
# URL: {'proper_name': 'Calendars', 'url': nan}
import pandas as pd
from autonomousAJ_googleCalendarAPI.api.calendars import Calendars
from autonomousAJ_googleCalendarAPI.config import global_config

class Calendars_Data:
    def __init__(self):
        self.calendars = Calendars()

    def get_and_process_data(self):
        data = self.calendars.get_calendars()
        df = pd.DataFrame(data)
        return df

    def save_data(self, df):
        # df.to_csv(FILE_PATH, index=False)
        print(df)
