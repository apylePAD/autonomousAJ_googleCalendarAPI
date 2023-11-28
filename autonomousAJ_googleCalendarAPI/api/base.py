# autonomousAJ_googleCalendarAPI/autonomousAJ_googleCalendarAPI/api/base.py
from autonomousAJ_googleCalendarAPI.auth import google_calendar_client
import requests

class Google_Calendar_API_Base:
    def get_google_calendar_client(self):
        return google_calendar_client.get_google_calendar_client()

    def get_api_url(self):
        return google_calendar_client.get_api_url()

    def handle_api_calls(self, api_function, *args, **kwargs):
        try:
            response = api_function(*args, **kwargs)
            response.raise_for_status()
            return response

        except requests.exceptions.HTTPError as errh:
            print(f"Http Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"OOps: Something Else {err}")
        except Exception as e:
            print(f"Error: {e}")

        return None
