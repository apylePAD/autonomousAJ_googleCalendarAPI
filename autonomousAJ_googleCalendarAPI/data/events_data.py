# autonomousAJ_googleCalendarAPI/autonomousAJ_googleCalendarAPI/data/events_data.py
# Endpoint: events
# URL: {'proper_name': 'Events', 'url': nan}
import pandas as pd
from autonomousAJ_googleCalendarAPI.api.events import Events
from autonomousAJ_googleCalendarAPI.config import global_config

class Events_Data:
    def __init__(self):
        self.events = Events()

    def get_and_process_data(self):
        data = self.events.get_events()
        df = pd.DataFrame(data)
        return df

    def save_data(self, df):
        # df.to_csv(FILE_PATH, index=False)
        print(df)
