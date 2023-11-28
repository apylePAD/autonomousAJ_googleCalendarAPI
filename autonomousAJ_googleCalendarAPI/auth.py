# autonomousAJ_googleCalendarAPI/autonomousAJ_googleCalendarAPI/auth.py
import os
from dotenv import load_dotenv

load_dotenv()

class Get_Google_Calendar_Client:
    def __init__(self):
        self.username = os.getenv("GOOGLE_CALENDAR_USERNAME")
        self.password = os.getenv("GOOGLE_CALENDAR_PASSWORD")

    def get_google_calendar_client(self):
        username = self.username
        password = self.password

        return clientusername, password

google_calendar_client = Get_Google_Calendar_Client()